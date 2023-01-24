import subprocess
import os

import telebot
from telebot import types

# import up
from key import key

bot = telebot.TeleBot(key)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard.row('Перевод раскладки ENG --> RUS', 'docker ps', 'Uptime')
    bot.send_message(message.chat.id, 'Привет, {0.first_name}! Чем могу помочь?'.format(message.from_user), reply_markup=keyboard)


def rasklad():
    eng = 'qwertyuiop[]asdfghjkl;\'\\zxcvbnm,.'
    rus = 'йцукенгшщзхъфывапролджэёячсмитьбю'

    trans = str.maketrans(eng, rus)

    answ = menu(msg).translate(trans)


@bot.message_handler(content_types='text')
def menu(message):
    keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
    keyboard1.row('Назад')
    if message.text == 'Перевод раскладки ENG --> RUS':
        msg = bot.send_message(message.chat.id, 'Введи текст:'.format(message.from_user), reply_markup=keyboard1)
        bot.register_next_step_handler(msg, rasklad())

    elif message.text == 'docker ps':
        doc = os.system('docker ps >> docker.txt && cat docker.txt')
        bot.send_message(message.chat.id, 'Контейнеры:'.format(message.from_user) + str(doc))

    elif message.text == 'Uptime':
        upt = subprocess.check_output(["uptime"]).decode('utf-8')
        bot.send_message(message.chat.id, 'Вот uptime сервера:\n'.format(message.from_user) + upt)


bot.polling(none_stop=True)
