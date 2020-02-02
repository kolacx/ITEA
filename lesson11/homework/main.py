from telebot import TeleBot
from config import TOKEN
from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
    )
from db_worker import (
    create_new_user, 
    set_user_name, 
    set_user_phone,
    set_user_email, 
    set_user_location,
    current_state, 
    set_state
    )

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def main_menu(message):

    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = [KeyboardButton('Да')]
    kb.add(*buttons)

    bot.send_message(message.chat.id, 'Привет, начнем?', reply_markup=kb)


@bot.message_handler(func=lambda message: current_state(message.chat.id) == 5)
def save_needs(message):
    set_user_needs(message.chat.id, message.text, 6)

    bot.send_message(message.chat.id, 'Адрес есть. Теперь Пожелание')


@bot.message_handler(func=lambda message: current_state(message.chat.id) == 4)
def save_location(message):
    set_user_location(message.chat.id, message.text, 5)

    bot.send_message(message.chat.id, 'Адрес есть. Теперь Пожелание')


@bot.message_handler(func=lambda message: current_state(message.chat.id) == 3)
def save_email(message):
    set_user_email(message.chat.id, message.text, 4)

    bot.send_message(message.chat.id, 'Емейл есть. Теперь Адресс')

@bot.message_handler(func=lambda message: current_state(message.chat.id) == 2)
def save_phone(message):
    set_user_phone(message.chat.id, message.text, 3)

    bot.send_message(message.chat.id, 'Телефон есть. Теперь Емейл')


@bot.message_handler(func=lambda message: current_state(message.chat.id) == 1)
def save_name(message):
    set_user_name(message.chat.id, message.text, 2)

    bot.send_message(message.chat.id, 'Имя есть. Теперь телефон')


@bot.message_handler(func=lambda message: message.text == 'Да')
def registration_start(message):

    create_new_user(message.chat.id, 1)

    bot.send_message(message.chat.id, 'Введи свое Имя.')



if __name__ == '__main__':
    bot.polling()