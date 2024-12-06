import json
import os
import numpy as np
import re
import pymorphy3
import spacy

from typing import Any, Dict, List, Tuple
from easydict import EasyDict
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from re import Match
from num2words import num2words
from spacy.lang.ru.stop_words import STOP_WORDS
from spacy.matcher import Matcher

os.environ["CURL_CA_BUNDLE"] = ""

model_cfg = EasyDict()
model_cfg.name_pretrained_model = "intfloat/multilingual-e5-small"
model_cfg.keyword_weight = 1
model_cfg.question_weight = 1
model_cfg.max_length = 128
model_cfg.input_weight = 1
model_cfg.num_questions = 7
model_cfg.threshold_similarity = 0.3
model_cfg.alpha = 0.5

main_cfg = EasyDict()
main_cfg.model = model_cfg

class TextProcessor:
    def __init__(self, max_length: int) -> None:
        """
        Инициализация текстового обработчика с использованием модели Spacy и Word2Vec.
        """
        self.nlp = spacy.load("ru_core_news_md")
        self.max_length = max_length
        self.stop_words = STOP_WORDS
        self.morph = pymorphy3.MorphAnalyzer()
        self.matcher = Matcher(self.nlp.vocab)

        custom_stop_words: Dict[str, Any] = {}
        self.stop_words = self.stop_words.union(custom_stop_words)

    def preprocess_to_bert(self, text: str) -> str:
        text = self.clean_text(text)
        return self.add_query(text)

    def clean_text(self, text: str) -> str:
        """
        Очистка текста: приведение к нижнему регистру, удаление пунктуации и чисел,
        а также приведение к единому пробельному символу.
        """
        if text is None:
            return ""

        text = text.lower()
        text = re.sub(r"[-–]", " ", text)
        text = re.sub(r"[^\w\s]", "", text)
        text = self._replace_digits_with_words(text)
        text = re.sub(r"https?://\S+|www\.\S+", "", text)
        text = re.sub(r"\s+", " ", text).strip()

        return text

    def add_query(self, text: str) -> str:
        return "query: " + text

    def _replace_digits_with_words(self, text: str) -> str:
        def replace_match(match: Match) -> str:
            num = match.group()
            try:
                return num2words(int(num), lang="ru")
            except (ValueError, NotImplementedError):
                return num

        return re.sub(r"\d+", replace_match, text)

    def summarize_text(self, text: str) -> str:
        """
        Суммаризация текста до заданной максимальной длины. Если текст превышает
        максимальную длину, он сокращается, сохраняя начало и конец.
        """
        tokens = text.split()
        if len(tokens) > self.max_length:
            tokens = tokens[: self.max_length // 2] + tokens[-self.max_length // 2 :]
        return " ".join(tokens)

    def extract_keywords(self, text: str) -> str:
        """
        Извлечение ключевых слов из текста, используя Spacy для лемматизации,
        удаления стоп-слов и обработки синтаксических зависимостей.
        """
        doc = self.nlp(text)

        keywords = [
            token.lemma_
            for token in doc
            if token.is_alpha
            and not token.is_stop
            and token.lemma_ not in self.stop_words
        ]

        keywords = [self.morph.parse(word)[0].normal_form for word in keywords]

        keywords = self._extract_with_dependencies(doc, keywords)

        return " ".join(keywords)

    def _extract_with_dependencies(
        self, doc: spacy.tokens.Doc, keywords: list[str]
    ) -> list[str]:
        """
        Дополнительное извлечение ключевых слов на основе синтаксических зависимостей.
        """
        for token in doc:
            if token.dep_ in ("amod", "acomp") and token.head.lemma_ in keywords:
                keywords.append(token.lemma_)
        return keywords



class Bert:
    def __init__(self, config: Any, data: List[Dict[str, Any]]) -> None:
        """
        Инициализация модели BERT с заданной конфигурацией.
        """
        self.config = config
        model_name = config.model.name_pretrained_model
        self.model = SentenceTransformer(model_name)
        self.keyword_weight = config.model.keyword_weight
        self.question_weight = config.model.question_weight
        self.input_weight = config.model.input_weight

        self.text_processor = TextProcessor(config.model.max_length)

        # Изменение: Создание BM25 модели
        self.bm25 = None
        self.corpus: List[List[str]] = []

        # Закодируем вопросы и сохраним их
        self.question_embeddings, self.questions = self._encode_questions(data)

    def _encode(self, texts: List[str]) -> Any:
        """
        Закодировать список текстов с использованием модели BERT.
        """
        embeddings = self.model.encode(texts)
        return embeddings

    def _encode_questions(
        self, qa_pairs: List[Dict[str, Any]]
    ) -> Tuple[np.ndarray, List[Tuple[Any, str]]]:
        """
        Закодировать вопросы и ответы из предоставленной базы данных.
        """
        combined_texts = []
        combined_texts_for_bert = []
        questions = []
        for pair in qa_pairs:
            id_question = pair["id"]
            question = pair["question"]
            keywords = pair.get("keyword", [])

            # Обработка и взвешивание вопросов
            summarized_question = " ".join(
                [
                    self.text_processor.extract_keywords(
                        self.text_processor.clean_text(
                            self.text_processor.summarize_text(question)
                        )
                    )
                    for _ in range(self.question_weight)
                ]
            )

            # Взвешивание ключевых слов
            weighted_keywords = " ".join(
                [
                    self.text_processor.extract_keywords(
                        self.text_processor.clean_text(kw)
                    )
                    for kw in keywords
                    for _ in range(self.keyword_weight)
                ]
            )

            combined_text = (
                f"{summarized_question} {weighted_keywords}"
            )
            combined_text_for_bert = (
                f"{self.text_processor.preprocess_to_bert(question)} "
                f"{weighted_keywords}"
            )
            combined_texts.append(combined_text)
            combined_texts_for_bert.append(combined_text_for_bert)
            questions.append((id_question, question))

        question_embeddings = self._encode(combined_texts_for_bert)

        # Изменение: Инициализация BM25 модели
        self.corpus = [doc.split(" ") for doc in combined_texts]
        self.bm25 = BM25Okapi(self.corpus)

        return np.array(question_embeddings), questions

    def find_top_n_similar_questions(
        self, input_text: str, top_n: int = 8
    ) -> List[Tuple[int, str, float]]:
        """
        Найти топ-N наиболее похожих вопросов на заданный входной текст.
        """

        preprocessed_input_text = " ".join(
            [
                self.text_processor.extract_keywords(
                    self.text_processor.clean_text(
                        self.text_processor.summarize_text(input_text)
                    )
                )
                for _ in range(self.input_weight)
            ]
        )
        preprocessed_input_text_to_bert = self.text_processor.preprocess_to_bert(
            input_text
        )
        input_text_encoded = self._encode([preprocessed_input_text_to_bert]).reshape(
            1, -1
        )
        similarities_bert = cosine_similarity(
            input_text_encoded, self.question_embeddings
        )
        tokenized_input = preprocessed_input_text.split(" ")

        if self.bm25 is not None:
            similarities_bm25 = self.bm25.get_scores(tokenized_input)
        else:
            similarities_bm25 = np.zeros(len(self.questions))

        # Нормализация сходств
        similarities_bert = (similarities_bert - np.min(similarities_bert)) / (
            np.max(similarities_bert) - np.min(similarities_bert)
        )
        similarities_bm25 = (similarities_bm25 - np.min(similarities_bm25)) / (
            np.max(similarities_bm25) - np.min(similarities_bm25)
        )

        if len(tokenized_input) < 4:
            similarities_bm25 *= 0.7

        # Комбинирование сходств с использованием веса alpha
        similarities = (
            self.config.model.alpha * similarities_bert[0]
            + (1 - self.config.model.alpha) * similarities_bm25
        )

        top_n_indices = similarities.argsort()[-top_n:][::-1]
        top_n_questions = [
            (self.questions[idx][0], self.questions[idx][1], similarities[idx])
            for idx in top_n_indices
        ]

        top_n_questions = [
            (self.questions[idx][0], self.questions[idx][1], similarities[idx])
            for idx in top_n_indices
            if similarities[idx] > self.config.model.threshold_similarity
        ]
        return top_n_questions

    def find_all_similar_questions(self, top_n: int = 3) -> Dict[int, List[Dict[str, Any]]]:
        """
        Найти топ-N наиболее похожих вопросов для каждого вопроса в базе данных.
        """
        result = {}
        for q_id, q_text in self.questions:
            top_similar = self.find_top_n_similar_questions(q_text, top_n=top_n)
            # Отфильтровываем текущий вопрос из результатов
            top_similar_filtered = [q for q in top_similar if q[0] != q_id]
            # Берем только первые top_n результатов после фильтрации
            top_similar_filtered = top_similar_filtered[:top_n]
            result[q_id] = [
                {
                    "id": sim_id,
                    "question": sim_q,
                    "similarity_score": round(sim_score, 4)
                }
                for sim_id, sim_q, sim_score in top_similar_filtered
            ]
        return result
    
def load_json(file_path: str) -> List[dict]:
    with open(file_path, 'r', encoding='utf-8') as file:
        questions = json.load(file)
    return questions

def extract_keywords_from_questions(input_json: List[dict]) -> List[dict]:
    questions = input_json.copy()

    text_processor = TextProcessor(max_length=128)
    for question in questions:
        cleaned_text = text_processor.clean_text(question["question"])
        keywords = text_processor.extract_keywords(cleaned_text)
        question["keywords"] = keywords

    return questions

def transform_json(input_json, column_name):
    transformed_data = [
        {"id": item["id"], "question": item[column_name]} for item in input_json
    ]
    return transformed_data

if __name__ == "__main__":
    json_name = "data.json"
    # На выбор: answer_job или answer_interests 
    column_name = "answer_interests"
    input_json = load_json(json_name)
    transformed_json = transform_json(input_json, column_name)
    questions_with_keywords = extract_keywords_from_questions(transformed_json)
    bert_model = Bert(main_cfg, questions_with_keywords)

    top_n = 3  # Количество похожих вопросов
    result = bert_model.find_all_similar_questions(top_n=top_n)
    print(json.dumps(result, ensure_ascii=False, indent=2))

    # СОХРАНЕНИЕ JSON
    output_filename = "similarity_results.json"

    # Записываем результат в файл
    output_path = os.path.join(output_filename)
    with open(output_path, 'w', encoding='utf-8') as json_file:
        json.dump(result, json_file, ensure_ascii=False, indent=2)