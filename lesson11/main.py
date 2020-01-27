from config import TOKEN
from words import GREETINGS, NEWS_TEXT
from keyboards import START_KB, NEWS_KB
from telebot import TeleBot
from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
    )

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_bot(message):

    # message.text - Tekst soobweniya
    # message.chat.id - Ид пользователя
    # message.from_user.id - Ид пользователя

    # print(message)

    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    buttons = [KeyboardButton(value) for value in START_KB.values()]

    kb.add(*buttons)

    bot.send_message(message.chat.id, 'Hello', reply_markup=kb)


@bot.message_handler(func=lambda message: message.text.lower() in GREETINGS.keys())
def hi(message):
    bot.send_message(message.chat.id, GREETINGS[message.text.lower()])




@bot.message_handler(func=lambda message: message.text == START_KB['main'])
def main(message):
    bot.send_message(message.chat.id, 
                    f'{GREETINGS["здравствуй"]} Ты на главной странице')


@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    bot.send_message(call.message.chat.id, NEWS_TEXT[call.data])


@bot.message_handler(func=lambda message: message.text == START_KB['news'])
def get_news(message):
    kb = InlineKeyboardMarkup(row_width=1)

    buttons = [InlineKeyboardButton(callback_data=str(key), text=value) 
                                    for key, value in NEWS_KB.items()]

    kb.add(*buttons)

    bot.send_message(message.chat.id, 'Выберите новость', reply_markup=kb)


@bot.message_handler(content_types=['text'])
def revers_message(message):

    text = message.text[::-1]

    bot.send_message(message.chat.id, text)







if __name__ == '__main__':
    bot.polling()