from telebot import TeleBot
from config import TOKEN
from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
    )

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def main_menu(message):

    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    buttons = [KeyboardButton('Да')]

    kb.add(*buttons)

    bot.send_message(message.chat.id, 'Привет, начнем?', reply_markup=kb)


@bot.message_handler(func=lambda message: message.text == 'Да')
def registration_name(message):

    bot.send_message(message.chat.id, 'Введи свое Имя.')


@bot.message_handler()
def registration_name(message):

    bot.send_message(message.chat.id, 'Введи свой Телефон.')

@bot.message_handler()
def registration_name(message):

    bot.send_message(message.chat.id, 'Введи свою Почту.')

if __name__ == '__main__':
    bot.polling()