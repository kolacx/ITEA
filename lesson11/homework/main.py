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
    set_user_needs,
    get_user,
    current_state
    )

bot = TeleBot(TOKEN)

# KeyboardButton - requestlocation=True

@bot.message_handler(commands=['start'])
def main_menu(message):

    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = [KeyboardButton('Да')]
    kb.add(*buttons)

    bot.send_message(message.chat.id, 'Привет, начнем?', reply_markup=kb)


@bot.message_handler(func=lambda message: message.text == 'Да')
def registration_start(message):

    create_new_user(str(message.chat.id), 1)

    bot.send_message(message.chat.id, 'Введи свое Имя.')

@bot.message_handler(func=lambda message: current_state(str(message.chat.id)) == 1)
def save_name(message):
    print('SaveName')
    set_user_name(str(message.chat.id), message.text, 2)

    bot.send_message(message.chat.id, 'Имя есть. Теперь телефон')

@bot.message_handler(func=lambda message: current_state(str(message.chat.id)) == 2)
def save_phone(message):
    print('SavePhone')
    set_user_phone(str(message.chat.id), message.text, 3)

    bot.send_message(message.chat.id, 'Телефон есть. Теперь Емейл')


@bot.message_handler(func=lambda message: current_state(str(message.chat.id)) == 3)
def save_email(message):
    print('SaveMail')
    set_user_email(str(message.chat.id), message.text, 4)

    bot.send_message(str(message.chat.id), 'Емейл есть. Теперь Адресс')

@bot.message_handler(func=lambda message: current_state(str(message.chat.id)) == 4)
def save_location(message):
    print('SaveAdres')
    set_user_location(str(message.chat.id), message.text, 5)

    bot.send_message(message.chat.id, 'Адрес есть. Теперь Пожелание')


@bot.message_handler(func=lambda message: current_state(str(message.chat.id)) == 5)
def save_needs(message):
    print('SaveNeeds')
    set_user_needs(str(message.chat.id), message.text, 6)

    bot.send_message(message.chat.id, 'End')


@bot.message_handler(func=lambda message: current_state(str(message.chat.id)) == 6)
def show_info(message):
    user = get_user(str(message.chat.id))

    mes = (f'Вот что ты ввел \n'
            f'Name: {user.username} \n'
            f'Phone: {user.phone_number} \n'
            f'Location: {user.location} \n'
            f'email: {user.email} \n'
            f'Needs: {user.needs}'
            )

    bot.send_message(message.chat.id, mes)

if __name__ == '__main__':
    bot.polling()