from config import TOKEN
from telebot import TeleBot 
from telebot import types

bot = TeleBot('1053710333:AAEJtQ9h_tE6BiUD6zGVnpfXmHeaDtuH_fk')
from keyboards import START_KB


@bot.message_handler(commands=['start'])
def start(message):
    buttons = START_KB.values()
    kb = types.InlineKeyboardMarkup()

    inline_button = [types.InlineKeyboardButton(text=button, switch_inline_query_current_chat=button) for button in buttons]
    kb.add(*inline_button)
    bot.send_message(message.chat.id, 'text', reply_markup=kb)


@bot.inline_handler(func=lambda query: True)
def inline(query):

    results = []

    for i in range(10):
        kb = types.InlineKeyboardMarkup()

        button = types.InlineKeyboardButton(text='Добавить в корзину', callback_data=str(i))

        kb.add(button)
        result1 = types.InlineQueryResultArticle(
                id=i,
                title='Nazvanie',
                description='Opisanie',
                input_message_content=types.InputTextMessageContent(
                    type='photo',
                    media='https://upload.wikimedia.org/wikipedia/en/4/4f/Under_construction.JPG',
                    caption='Opisanie'
                    ),
                # input_message_content=types.InputTextMessageContent(message_text='Текст после нажатия на инлайн кнопку'),
                thumb_url='https://upload.wikimedia.org/wikipedia/en/4/4f/Under_construction.JPG',
                reply_markup=kb
            )
        results.append(result1)

    bot.answer_inline_query(query.id, results, cache_time=0)


@bot.chosen_inline_handler(func=lambda chosen_result: True)
def chosen_result_(chosen_result):
    print(chosen_result)


bot.polling()