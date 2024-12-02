import telebot
from datetime import datetime
from constants import MESSAGES


token = ('7916244383:AAFccoAAoG5e_BA_s_yVN0_zvJqpTDbp2-U')
bot = telebot.TeleBot(token)

user_dict = {}
groups = ['default']


@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton(text="Поехали!", callback_data='start_collecting_data')
    keyboard.add(button)
    #with open('C:\\Users\\79851\\Downloads\\Hello.jpg', 'rb') as file:
    #    photo = file.read()
    #bot.send_photo(chat_id, photo)
    username = message.from_user.first_name
    user_dict[chat_id] = {}
    user_dict[chat_id]['id'] = message.from_user.id
    user_dict[chat_id]['user_name'] = f'@{message.from_user.username}'
    user_dict[chat_id]['filled'] = False
    bot.send_message(chat_id, MESSAGES['StartMsg'].format(username=username), reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def bot_help(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_view_profile = telebot.types.InlineKeyboardButton(text='Посмотреть профиль', callback_data='view_profile')
    button_change_profile = telebot.types.InlineKeyboardButton(text='Поменять данные профиля', callback_data='edit_profile')
    button_change_groups = telebot.types.InlineKeyboardButton(text='Изменить группы', callback_data='edit_groups')
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


@bot.callback_query_handler(func=lambda call: call.data == 'rate_meeting')
def rate(call):
    last_partner = None
    for chat_id in user_dict:
        if chat_id != call.message.chat.id:
            last_partner = user_dict[chat_id]['user_name']
    if last_partner:
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton(text='1', callback_data='rate1')
        button_2 = telebot.types.InlineKeyboardButton(text='2', callback_data='rate1')
        button_3 = telebot.types.InlineKeyboardButton(text='3', callback_data='rate1')
        button_4 = telebot.types.InlineKeyboardButton(text='4', callback_data='rate1')
        button_5 = telebot.types.InlineKeyboardButton(text='5', callback_data='rate1')
        keyboard.add(button_1, button_2, button_3, button_4, button_5)
        bot.send_message(chat_id=call.message.chat.id, text=f'Оцените встречу с {last_partner}', reply_markup=keyboard)
    else:
        bot.send_message(chat_id=call.message.chat.id, text='У Вас пока что не было встреч')


@bot.callback_query_handler(func=lambda call: call.data == 'edit_groups')
def edit_groups(call):
    ask_group(call.message)


@bot.callback_query_handler(func=lambda call: call.data == 'pause_bot')
def stop_bot(call):
    bot.send_message(chat_id=call.message.chat.id, text='Бот поставлен на паузу')


@bot.callback_query_handler(func=lambda call: call.data == 'stop_pause_bot')
def stop_pause_bot(call):
    bot.send_message(chat_id=call.message.chat.id, text='Бот снят с паузы')


@bot.callback_query_handler(func=lambda call: call.data == 'view_profile')
def view_profile_call(call):
    view_profile(call.message)


def view_profile(message):
    user = user_dict[message.chat.id]
    text = MESSAGES['ViewMsg'].format(
        full_name=user['full_name'],
        user_name=user['user_name'],
        city=user['city'],
        birthday=user['birthday'].strftime('%d.%m.%Y'),
        position=user['position'],
        interests=user['interests'],
        socials=user['socials']
    )
    if user['photo_url']:
        bot.send_photo(message.chat.id, user['photo_url'], caption=text)
    else:
        bot.send_message(chat_id=message.chat.id, text=text)


@bot.callback_query_handler(func=lambda call: call.data == 'edit_profile')
def edit_profile(call):
    view_profile(call.message)
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
    bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=call.message.text)
    bot.register_next_step_handler(call.message, save_name)


def save_name(message):
    user_dict[message.chat.id]['full_name'] = message.text
    if not user_dict[message.chat.id]['filled']:
        ask_gender(message)


def ask_gender(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_male = telebot.types.InlineKeyboardButton(text="Мужчина", callback_data='male_gender_save')
    button_female = telebot.types.InlineKeyboardButton(text="Женщина", callback_data='female_gender_save')
    keyboard.add(button_male, button_female)
    bot.send_message(chat_id=message.chat.id, text=MESSAGES['GenderMsg'], reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: 'gender' in call.data)
def save_gender(call):
    user_dict[call.message.chat.id]['gender'] = call.data.split('_gender')[0]
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text)
    if not user_dict[call.message.chat.id]['filled']:
        ask_photo(call.message)


def ask_photo(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_save = telebot.types.KeyboardButton(text="Возьмите аватарку")
    keyboard.add(button_save)
    bot.send_message(chat_id=message.chat.id, text=MESSAGES['PhotoMsg'], reply_markup=keyboard)


@bot.message_handler(content_types=['photo'])
def photo_id(message):
    photo = max(message.photo, key=lambda x: x.height)
    user_dict[message.chat.id]['photo_url'] = photo.file_id
    if not user_dict[message.chat.id]['filled']:
        ask_city(message)


@bot.message_handler(func=lambda message: message.text == 'Возьмите аватарку')
def take_avatar_photo(message):
    photos = bot.get_user_profile_photos(message.from_user.id)
    if photos.total_count > 0:
        photo = photos.photos[0][-1]
    else:
        photo = None
    if photo:
        user_dict[message.chat.id]['photo_url'] = photo.file_id
    if not user_dict[message.chat.id]['filled']:
        ask_city(message)


def ask_city(message):
    keyboard = telebot.types.ReplyKeyboardRemove()
    bot.send_message(chat_id=message.chat.id, text=MESSAGES['CityMsg'], reply_markup=keyboard)
    bot.register_next_step_handler(message, save_city)


def save_city(message):
    user_dict[message.chat.id]['city'] = message.text
    if not user_dict[message.chat.id]['filled']:
        ask_socials(message)


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
        bot.send_message(chat_id=message.chat.id, text='Введите действительную ссылку')
        bot.register_next_step_handler(message, save_socials)


def ask_position(message):
    bot.send_message(chat_id=message.chat.id, text=MESSAGES['PositionMsg'])
    bot.register_next_step_handler(message, save_position)


def save_position(message):
    user_dict[message.chat.id]['position'] = message.text
    if not user_dict[message.chat.id]['filled']:
        ask_interests(message)


def ask_interests(message):
    bot.send_message(chat_id=message.chat.id, text=MESSAGES['InterestsMsg'])
    bot.register_next_step_handler(message, save_interests)


def save_interests(message):
    user_dict[message.chat.id]['interests'] = message.text
    if not user_dict[message.chat.id]['filled']:
        ask_birthday(message)


def ask_birthday(message):
    bot.send_message(chat_id=message.chat.id, text=MESSAGES['BirthdayMsg'])
    bot.register_next_step_handler(message, save_birthday)


def save_birthday(message):
    user_dict[message.chat.id]['birthday'] = datetime.strptime(message.text, '%d.%m.%Y')
    if not user_dict[message.chat.id]['filled']:
        ask_goal(message)


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
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text)
    if not user_dict[call.message.chat.id]['filled']:
        ask_group(call.message)


def ask_group(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_save = telebot.types.InlineKeyboardButton(text="Не знаю")
    keyboard.add(button_save)
    bot.send_message(chat_id=message.chat.id, text=MESSAGES['GroupMsg'], reply_markup=keyboard)
    bot.register_next_step_handler(message, save_group)


def save_group(message):
    global groups
    if message.text == 'Не знаю':
        user_dict[message.chat.id]['groups'] = [{'id': 0, 'name': 'default'}]
    else:
        if message.text not in groups:
            groups += [message.text]
        user_dict[message.chat.id]['groups'] = [{'id': groups.index(message.text), 'name': message.text}]
    if not user_dict[message.chat.id]['filled']:
        user_dict[message.chat.id]['filled'] = True
        keyboard = telebot.types.ReplyKeyboardRemove()
        bot.send_message(chat_id=message.chat.id, text=MESSAGES['CheckProfileMsg'], reply_markup=keyboard)
        view_profile(message)


if __name__ == '__main__':
    print('Бот запущен!')
    bot.infinity_polling()
