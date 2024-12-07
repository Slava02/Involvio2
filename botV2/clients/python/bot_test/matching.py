import telebot
import schedule
import time
import json
import random

with open('users.json', 'r') as file:
    user_dict = json.load(file)

from bot import token, view_profile

bot = telebot.TeleBot(token)

groups = []
for user in user_dict:
    if user_dict[user]['group']['name'] not in groups:
        groups.append(user_dict[user]['group']['name'])


pair_limits = {}
old_pairs = {}
unhappy_users = {}

for group in groups:
    old_pairs[group] = []
    unhappy_users[group] = []
    pair_limits[group] = None

new_pairs = {}


def obj_in_double_level_list(obj, iter):
    for i in iter:
        if obj in i:
            return True
    return False


def match():
    group_dict = {}

    for group in groups:
        group_dict[group] = []
        for user in user_dict:
            if user_dict[user]['group']['name'] == group:
                group_dict[group] += [user]

    for group in group_dict:

        new_pairs[group] = find_new_pairs(group, group_dict)

        old_pairs[group] += new_pairs[group]
        if new_pairs[group] == old_pairs[group]:
            pair_limits[group] = len(old_pairs[group])
        for user in group_dict[group]:
            if not obj_in_double_level_list(user, new_pairs[group]):
                print(f'{user_dict[user]['user_name']} has no pair this time :(')
                unhappy_users[group] += [user]
                bot.send_message(chat_id=user, text='Вам сегодня пара не найдена.\n\nНе отчаивайтесь, мы постараемся подобрать вам достойного собеседника при первой возможности!')
        for pair in new_pairs[group]:
            print(f'{user_dict[pair[0]]['user_name']}, {user_dict[pair[1]]['user_name']}')
            for user in pair:
                bot.send_message(chat_id=user, text='Твоя пара на эту неделю:')
                view_profile(user_id=pair[(pair.index(user)+1) % 2], chat_id=user, users=user_dict, tbot=bot, help_message=False)

    with open('pairs.json', 'w') as file:
        json.dump(new_pairs, file)


def find_new_pairs(group, group_dict):
    if len(group_dict[group]) % 2 == 1:
        new_unhappy_users = list(set(group_dict[group]) - set(unhappy_users[group]))
        if not new_unhappy_users:
            new_unhappy_users = group_dict[group]
            unhappy_users[group] = []
        unhappy_user = [new_unhappy_users[random.randint(0, len(new_unhappy_users) - 1)]]
        users = list(set(group_dict[group]) - set(unhappy_user))
    else:
        users = group_dict[group].copy()

    new_pairs = []
    for user1 in users:
        if obj_in_double_level_list(user1, new_pairs):
            continue
        group_list = users.copy()
        for user2 in users:
            if ((user1, user2) in old_pairs[group] or (user2, user1) in old_pairs[group] or obj_in_double_level_list(
                    user2, new_pairs)) and user2 in group_list:
                group_list.remove(user2)
        if user1 in group_list:
            group_list.remove(user1)
        if group_list:
            new_pairs.append((user1, group_list[random.randint(0, len(group_list) - 1)]))
    if pair_limits[group] and len(new_pairs) < pair_limits[group]:
        old_pairs[group] = []
        new_pairs = find_new_pairs(group, group_dict)
    return new_pairs


if __name__ == '__main__':

    schedule.every().thursday.at("21:43", "Europe/Moscow").do(match)

    while True:
        schedule.run_pending()
        time.sleep(1)
