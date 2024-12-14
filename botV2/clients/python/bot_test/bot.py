import telebot
from datetime import datetime
import json
from cities import main
from constants import MESSAGES

token = ('7916244383:AAFccoAAoG5e_BA_s_yVN0_zvJqpTDbp2-U')
bot = telebot.TeleBot(token)


user_dict = {}
rating = {}
groups = ['default']

try:
    with open('users.json', 'r') as file:
        u_dict = json.load(file)
        for user in u_dict:
            user_dict[int(user)] = u_dict[user]
            rating[int(user)] = {}
            if u_dict[user]['group']['name'] not in groups:
                groups.append(u_dict[user]['group']['name'])
except:
    pass

active_users = []


@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton(text="Поехали!", callback_data='start_collecting_data')
    keyboard.add(button)
    username = message.from_user.first_name
    rating[chat_id] = {}
    user_dict[chat_id] = {}
    user_dict[chat_id]['id'] = message.from_user.id
    user_dict[chat_id]['user_name'] = f'@{message.from_user.username}'
    user_dict[chat_id]['full_name'] = f'{message.from_user.first_name} {message.from_user.last_name}'
    user_dict[chat_id]['blocked'] = []
    user_dict[chat_id]['filled'] = False
    bot.send_message(chat_id, MESSAGES['StartMsg'].format(username=username), reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def bot_help(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_view_profile = telebot.types.InlineKeyboardButton(text='Посмотреть профиль', callback_data='view_profile')
    button_change_profile = telebot.types.InlineKeyboardButton(text='Поменять данные профиля', callback_data='edit_profile')
    button_change_groups = telebot.types.InlineKeyboardButton(text='Изменить группу', callback_data='edit_groups')
    button_pause_bot = telebot.types.InlineKeyboardButton(text='Поставить бот на паузу', callback_data='pause_bot')
    button_stop_pause_bot = telebot.types.InlineKeyboardButton(text='Снять бот с паузы', callback_data='stop_pause_bot')
    button_rate_meeting = telebot.types.InlineKeyboardButton(text='Оценить встречу', callback_data='rate_meeting')
    button_block_user = telebot.types.InlineKeyboardButton(text='Заблокировать пользователя', callback_data='block_user')
    keyboard.add(button_view_profile)
    keyboard.add(button_change_profile)
    keyboard.add(button_change_groups)
    keyboard.add(button_pause_bot)
    keyboard.add(button_stop_pause_bot)
    keyboard.add(button_rate_meeting)
    keyboard.add(button_block_user)
    bot.send_message(chat_id=message.chat.id, text=MESSAGES['HelpMsg'], reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'block_user')
def block_user(call):
    if user_dict[call.message.chat.id]['blocked']:
        bot.send_message(chat_id=call.message.chat.id,
                     text=f'Список заблокированных пользователей: {', '.join(user_dict[call.message.chat.id]['blocked'])}')
    bot.send_message(chat_id=call.message.chat.id, text='Чтобы заблокировать пользователя, введи его username (начинается с символа @)')
    bot.register_next_step_handler(call.message, get_block)


def get_block(message):
    user_dict[message.chat.id]['blocked'].append(message.text)
    with open('users.json', 'w') as file:
        json.dump(user_dict, file)
    bot.send_message(chat_id=message.chat.id, text=f'Список заблокированных пользователей: {', '.join(user_dict[message.chat.id]['blocked'])}')



@bot.callback_query_handler(func=lambda call: call.data == 'rate_meeting')
def rate(call):
    last_partner = None
    try:
        with open('pairs.json', 'r') as file:
            pairs = json.load(file)
        for group in pairs:
            for pair in pairs[group]:
                if str(call.message.chat.id) in pair:
                    last_partner = pair[(pair.index(str(call.message.chat.id))+1) % 2]
    except:
        pass
    if last_partner:
        try:
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=5)
            button_1 = telebot.types.InlineKeyboardButton(text='1', callback_data='rate1')
            button_2 = telebot.types.InlineKeyboardButton(text='2', callback_data='rate2')
            button_3 = telebot.types.InlineKeyboardButton(text='3', callback_data='rate3')
            button_4 = telebot.types.InlineKeyboardButton(text='4', callback_data='rate4')
            button_5 = telebot.types.InlineKeyboardButton(text='5', callback_data='rate5')
            keyboard.add(button_1, button_2, button_3, button_4, button_5)
            bot.send_message(chat_id=call.message.chat.id, text=f'Как прошла твоя встреча с {user_dict[int(last_partner)]['user_name']} на этой неделе?\nОцени общее впечатление по 5-баль﻿ной шкале, где 5 - отлично', reply_markup=keyboard)
            rating[call.message.chat.id][user_dict[int(last_partner)]['user_name']] = {}
        except:
            bot.send_message(chat_id=call.message.chat.id, text='У тебя пока что не было встреч')
    else:
        bot.send_message(chat_id=call.message.chat.id, text='У Вас тебя что не было встреч')


@bot.callback_query_handler(func=lambda call: 'rate' in call.data)
def rate_result(call):
    last_partner = list(rating[call.message.chat.id].keys())[-1]
    rating[call.message.chat.id][last_partner] = {'rate': call.data.split('rate')[1]}
    bot.send_message(chat_id=call.message.chat.id, text=MESSAGES['CommentMsg'])
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text)
    bot.register_next_step_handler(call.message, answer_written)


def answer_written(message):
    last_partner = list(rating[message.chat.id].keys())[-1]
    rating[message.chat.id][last_partner]['comment'] = message.text
    bot.send_message(chat_id=message.chat.id, text='Ваш ответ записан. Спасибо за обратную связь!')


@bot.message_handler(commands=['stat'])
def send_statistics(message):
    text = f'Проведено встреч: {len(rating[message.chat.id])}'
    for rate in rating[message.chat.id]:
        text += f'\n\n{rate}: {rating[message.chat.id][rate]['rate']}, {rating[message.chat.id][rate]['comment']}'
    bot.send_message(chat_id=message.chat.id, text=text)


@bot.callback_query_handler(func=lambda call: call.data == 'edit_groups')
def edit_groups(call):
    bot.send_message(chat_id=call.message.chat.id, text=f'Ваша текущая группа: {user_dict[call.message.chat.id]['group']['name']}')
    ask_group(call.message)


@bot.callback_query_handler(func=lambda call: call.data == 'pause_bot')
def stop_bot(call):
    bot.send_message(chat_id=call.message.chat.id, text='Бот поставлен на паузу')


@bot.callback_query_handler(func=lambda call: call.data == 'stop_pause_bot')
def stop_pause_bot(call):
    bot.send_message(chat_id=call.message.chat.id, text='Бот снят с паузы')


@bot.callback_query_handler(func=lambda call: call.data == 'view_profile')
def view_profile_call(call):
    view_profile(call.message.chat.id, call.message.chat.id)


def view_profile(user_id, chat_id, users=user_dict, tbot=bot, help_message: bool = True):
    user = users[user_id]
    text = MESSAGES['ViewMsg'].format(
        full_name=user['full_name'],
        user_name=user['user_name'],
        city=user['city'],
        birthday=user['birthday'],
        position=user['position'],
        interests=user['interests'],
        socials=user['socials']
    )
    if user['photo_url']:
        tbot.send_photo(chat_id, user['photo_url'], caption=text)
    else:
        tbot.send_message(chat_id=chat_id, text=text)
    if help_message:
        tbot.send_message(chat_id=chat_id, text='Если нужно что-то поменять, поможет команда /help')


@bot.callback_query_handler(func=lambda call: call.data == 'edit_profile')
def edit_profile(call):
    view_profile(call.message.chat.id, call.message.chat.id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_edit_name = telebot.types.InlineKeyboardButton(text='Имя и Фамилию', callback_data='start_collecting_data')
    button_edit_city = telebot.types.InlineKeyboardButton(text='Город', callback_data='edit_city')
    button_edit_position = telebot.types.InlineKeyboardButton(text='Род занятий', callback_data='edit_position')
    button_edit_interests = telebot.types.InlineKeyboardButton(text='Интересы', callback_data='edit_interests')
    button_edit_photo = telebot.types.InlineKeyboardButton(text='Фото', callback_data='edit_photo')
    keyboard.add(button_edit_name)
    keyboard.add(button_edit_city)
    keyboard.add(button_edit_position)
    keyboard.add(button_edit_interests)
    keyboard.add(button_edit_photo)
    bot.send_message(chat_id=call.message.chat.id, text='Выберите, что бы Вы хотели поменять:', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'edit_city')
def edit_city(call):
    ask_city(call.message)


@bot.callback_query_handler(func=lambda call: call.data == 'edit_position')
def edit_position(call):
    ask_position(call.message)


@bot.callback_query_handler(func=lambda call: call.data == 'edit_interests')
def edit_interests(call):
    ask_interests(call.message)


@bot.callback_query_handler(func=lambda call: call.data == 'edit_photo')
def edit_photo(call):
    ask_photo(call.message)


@bot.callback_query_handler(func=lambda call: call.data == 'start_collecting_data')
def ask_name(call):
    chat_id = call.message.chat.id
    bot.send_message(chat_id=chat_id, text=MESSAGES['NameMsg'])
    bot.register_next_step_handler(call.message, save_name)


def save_name(message):
    user_dict[message.chat.id]['full_name'] = message.text
    if not user_dict[message.chat.id]['filled']:
        ask_gender(message)
    else:
        with open('users.json', 'w') as file:
            json.dump(user_dict, file)
            view_profile(message.chat.id, message.chat.id)



def ask_gender(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_male = telebot.types.InlineKeyboardButton(text="Мужчина", callback_data='male_gender_save')
    button_female = telebot.types.InlineKeyboardButton(text="Женщина", callback_data='female_gender_save')
    keyboard.add(button_male, button_female)
    bot.send_message(chat_id=message.chat.id, text=MESSAGES['GenderMsg'], reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: 'gender' in call.data)
def save_gender(call):
    user_dict[call.message.chat.id]['gender'] = call.data.split('_gender')[0]
    if not user_dict[call.message.chat.id]['filled']:
        ask_photo(call.message)
    else:
        with open('users.json', 'w') as file:
            json.dump(user_dict, file)


def ask_photo(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_save = telebot.types.InlineKeyboardButton(text="Отправить фото профиля", callback_data='take_avatar_photo')
    keyboard.add(button_save)
    bot.send_message(chat_id=message.chat.id, text=MESSAGES['PhotoMsg'], reply_markup=keyboard)


@bot.message_handler(content_types=['photo'])
def photo_id(message):
    photo = max(message.photo, key=lambda x: x.height)
    user_dict[message.chat.id]['photo_url'] = photo.file_id
    if not user_dict[message.chat.id]['filled']:
        ask_city(message)
    else:
        with open('users.json', 'w') as file:
            json.dump(user_dict, file)
            view_profile(message.chat.id, message.chat.id)


@bot.callback_query_handler(func=lambda call: call.data == 'take_avatar_photo')
def take_avatar_photo(call):
    photos = bot.get_user_profile_photos(user_dict[call.message.chat.id]['id'])
    photo = photos.photos[0][-1] if photos.total_count > 0 else None
    user_dict[call.message.chat.id]['photo_url'] = photo.file_id if photo else None
    if not user_dict[call.message.chat.id]['filled']:
        ask_city(call.message)
    else:
        with open('users.json', 'w') as file:
            json.dump(user_dict, file)
            view_profile(message.chat.id, message.chat.id)


def ask_city(message):
    keyboard = telebot.types.ReplyKeyboardRemove()
    bot.send_message(chat_id=message.chat.id, text=MESSAGES['CityMsg'], reply_markup=keyboard)
    bot.register_next_step_handler(message, save_city)


def save_city(message):
    if main(message.text):
        user_dict[message.chat.id]['city'] = message.text
        if not user_dict[message.chat.id]['filled']:
            ask_socials(message)
        else:
            with open('users.json', 'w') as file:
                json.dump(user_dict, file)
            view_profile(message.chat.id, message.chat.id)
    else:
        bot.send_message(chat_id=message.chat.id, text='Введи сущесвтующий город')
        bot.register_next_step_handler(message, save_city)


def ask_socials(message):
    bot.send_message(chat_id=message.chat.id, text=MESSAGES['SocialsMsg'])
    bot.register_next_step_handler(message, save_socials)


def save_socials(message):
    socials = message.text
    if 'https://' in socials:
        user_dict[message.chat.id]['socials'] = socials
        if not user_dict[message.chat.id]['filled']:
            ask_position(message)
        else:
            with open('users.json', 'w') as file:
                json.dump(user_dict, file)
            view_profile(message.chat.id, message.chat.id)
    else:
        bot.send_message(chat_id=message.chat.id, text='Введи действительную ссылку')
        bot.register_next_step_handler(message, save_socials)


def ask_position(message):
    bot.send_message(chat_id=message.chat.id, text=MESSAGES['PositionMsg'])
    bot.register_next_step_handler(message, save_position)


def save_position(message):
    user_dict[message.chat.id]['position'] = message.text
    if not user_dict[message.chat.id]['filled']:
        ask_interests(message)
    else:
        with open('users.json', 'w') as file:
            json.dump(user_dict, file)
        view_profile(message.chat.id, message.chat.id)


def ask_interests(message):
    bot.send_message(chat_id=message.chat.id, text=MESSAGES['InterestsMsg'])
    bot.register_next_step_handler(message, save_interests)


def save_interests(message):
    user_dict[message.chat.id]['interests'] = message.text
    if not user_dict[message.chat.id]['filled']:
        ask_birthday(message)
    else:
        with open('users.json', 'w') as file:
            json.dump(user_dict, file)
        view_profile(message.chat.id, message.chat.id)


def ask_birthday(message):
    bot.send_message(chat_id=message.chat.id, text=MESSAGES['BirthdayMsg'])
    bot.register_next_step_handler(message, save_birthday)


def save_birthday(message):
    try:
        date = datetime.strptime(message.text, '%d.%m.%Y')
        user_dict[message.chat.id]['birthday'] = message.text
        if not user_dict[message.chat.id]['filled']:
            ask_goal(message)
        else:
            with open('users.json', 'w') as file:
                json.dump(user_dict, file)
            view_profile(message.chat.id, message.chat.id)
    except ValueError:
        bot.send_message(chat_id=message.chat.id, text='Введите корректную дату в формате ДД.ММ.ГГГГ')
        bot.register_next_step_handler(message, save_birthday)


def ask_goal(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_fan = telebot.types.InlineKeyboardButton(text="Фан", callback_data='goal_fan')
    button_profit = telebot.types.InlineKeyboardButton(text="Польза", callback_data='goal_profit')
    button_50 = telebot.types.InlineKeyboardButton(text="50/50", callback_data='goal_50/50')
    keyboard.add(button_fan, button_profit, button_50)
    bot.send_message(chat_id=message.chat.id, text=MESSAGES['GoalMsg'], reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: 'goal' in call.data)
def save_goal(call):
    user_dict[call.message.chat.id]['goal'] = call.data.split('goal_')[1]
    if not user_dict[call.message.chat.id]['filled']:
        ask_group(call.message)
    else:
        with open('users.json', 'w') as file:
            json.dump(user_dict, file)


def ask_group(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_save = telebot.types.InlineKeyboardButton(text="Не знаю", callback_data='no_group')
    button1 = telebot.types.InlineKeyboardButton(text="Ввести код группы", callback_data='enter_group')
    keyboard.add(button_save, button1)
    bot.send_message(chat_id=message.chat.id, text=MESSAGES['GroupMsg'], reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'no_group')
def no_group(call):
    user_dict[call.message.chat.id]['group'] = {'id': 0, 'name': 'default'}
    bot.send_message(chat_id=call.message.chat.id, text=f'Участники будут подбираться только из группы с кодом: {user_dict[call.message.chat.id]['group']['name']}')
    with open('users.json', 'w') as file:
        json.dump(user_dict, file)
    if not user_dict[call.message.chat.id]['filled']:
        user_dict[call.message.chat.id]['filled'] = True
        bot.send_message(chat_id=call.message.chat.id, text=MESSAGES['CheckProfileMsg'].format(group=user_dict[call.message.chat.id]['group']['name']))
        view_profile(call.message.chat.id, call.message.chat.id)


@bot.callback_query_handler(func=lambda call: call.data == 'enter_group')
def enter_group(call):
    bot.send_message(chat_id=call.message.chat.id, text='Теперь введи код:')
    bot.register_next_step_handler(call.message, save_group)


def save_group(message):
    global groups
    if message.text not in groups:
        groups += [message.text]
        bot.send_message(chat_id=message.chat.id,  text='В этой группе ты первый участник!')
    user_dict[message.chat.id]['group'] = {'id': groups.index(message.text), 'name': message.text}
    with open('users.json', 'w') as file:
        json.dump(user_dict, file)
    bot.send_message(chat_id=message.chat.id, text=f'Участники будут подбираться только из группы с кодом: {user_dict[message.chat.id]['group']['name']}')
    if not user_dict[message.chat.id]['filled']:
        user_dict[message.chat.id]['filled'] = True
        bot.send_message(chat_id=message.chat.id, text=MESSAGES['CheckProfileMsg'].format(group=user_dict[message.chat.id]['group']['name']))
        view_profile(message.chat.id, message.chat.id)


@bot.callback_query_handler(func=lambda call: call.data in ['yes', 'no'])
def answer(call):
    global active_users
    if call.data == 'yes':
        message = 'Ищу тебе пару!\nКак только найду, обязательно сообщу!'
        active_users += [call.message.chat.id]
        with open('active_users.json', 'w') as file:
            json.dump(active_users, file)

    else:
        message = 'Если хочешь приостановить бота, можешь воспользоваться командой: /help\n\nДо встречи!'
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text)
    bot.send_message(chat_id=call.message.chat.id, text=message)


if __name__ == '__main__':
    print('Бот запущен!')
    bot.infinity_polling()
