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
                    title='Назвdasdasdasdasdasание',
                    description='Опиdasdсание',
                    thumb_url='https://s.ftcdn.net/v2013/pics/all/curated/RKyaEDwp8J7JKeZWQPuOVWvkUjGQfpCx_cover_580.jpg',
                    reply_markup=kb,

                    input_message_content=types.InputTextMessageContent(
                        parse_mode='HTML',
                        disable_web_page_preview=False,
                        message_text="dasdasda <a href='https://s.ftcdn.net/v2013/pics/all/curated/RKyaEDwp8J7JKeZWQPuOVWvkUjGQfpCx_cover_580.jpg'>&#8204</a>"
                    )


                )
        results.append(result1)

    bot.answer_inline_query(query.id, results, cache_time=0)


@bot.chosen_inline_handler(func=lambda chosen_result: True)
def chosen_result_(chosen_result):
    print(chosen_result)


bot.polling()