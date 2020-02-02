from telebot import TeleBot
from config import TOKEN
from models.model import Category, Product, Texts
from keyboards import START_KB
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

bot = TeleBot(token=TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    txt = Texts.objects.filter(
        text_type='Greeting'
        ).get()

    kb = ReplyKeyboardMarkup(one_time_keyboard=True)
    buttons = [KeyboardButton(button_name) for button_name in START_KB.values()]
    kb.add(*buttons)

    bot.send_message(message.chat.id, txt.body, reply_markup=kb)

# @bot.callback_query_handler(func=lambda call: True)
# def callback_subcategory(call):
#      print(call.data)

#      sub_category = Category.objects.filter(
        
#         )

@bot.message_handler(func=lambda message: message.text == START_KB['categories'])
def show_news(message):
    category = Category.objects.filter(
            subcategories=[]
        )

    for cat in category:
        mes = (f'{cat.title} \n' 
                f'{cat.description}')

        kb = InlineKeyboardMarkup(row_width=1)
        buttons = [InlineKeyboardButton(callback_data=cat.title, text='Перейти в категорию')]
        kb.add(*buttons)

        bot.send_message(message.chat.id, mes, reply_markup=kb)



if __name__ == '__main__':
    bot.polling()