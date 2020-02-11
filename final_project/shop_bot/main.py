from bot import TGbot
from config import TOKEN
from models.model import Category, Product, Texts, Cart
from keyboards import START_KB
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

bot = TGbot(token=TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_start(message.chat.id)


@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'category')
def get_cat_or_products(call):
    print('callback_query_handler Category')
    category_id = call.data.split('_')[1]

    bot.subcategories_or_products(category_id, call.message.message_id, call.message.chat.id, 'Выберите подкатегорию' )


@bot.callback_query_handler(func=lambda call: call.data == START_KB['categories'])
def get_root_category(call):
    print('get_root_category')

    bot.root_categories(call.from_user.id, 'Выберите категорию')


@bot.inline_handler(func=lambda query: query.query.split('_')[0] == 'category')
def category(query):
    print('inline_handler Category')
    category_id = query.query.split('_')[1]

    bot.subcategories_or_products(category_id, query.id, query.from_user.id, 'Выберите подкатегорию' )


@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'product')
def add_to_card(call):
    print('Add to Card')

    prod_id = call.data.split('_')[1]
    user_id = call.message.chat.id

    cart = Cart.get_or_create_cart(user_id)

    cart.add_product_to_cart(product_id=prod_id)

    # tyt pop up naiti Тут поп ап найти

"""
WEBHOOK_HOST = https://33.46.22.19:8443

PKEM = '/home/sertificates/webhok_pkem.pem'
PKEY = '/home/sertificates/webhok_pkey.pem'

bot.set_webhook(WEBHOOK_HOST, open('r', PKEM))

TimeLoop - cron

sendChatAction - ... 'typing'

нджинкс - всджиай - питон

VPS - mesto na polwoi mawine
VDS - Fiz machin

WebServer - прилодение програма которая работает на сервере (Сервер)Принять данные вернуть данные. 
Веб сервер получил запрос передает в програму програма возвращяет веб серверу на отправку
Server - 
Порты - Как дом и квартиры Квартиры ето порты

"""

if __name__ == '__main__':
    bot.polling()