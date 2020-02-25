# from bot import TGbot
from config import TOKEN, WEBHOOK_URL, PATH, bot, app
from models.model import Category, Product, Texts, Cart, User
from keyboards import START_KB
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, Update
from flask import request, abort
import utils

'''
Вынести БОТ в ботПиВай и импортировать его в мейн и в утилс
'''

# bot = TGbot(token=TOKEN)

# app = Flask(__name__)


@app.route(f'/{PATH}', methods=['POST'])
def webhook():
    """
    Function process webhook call
    """
    if request.headers.get('content-type') == 'application/json':

        json_string = request.get_data().decode('utf-8')
        update = Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''

    else:
        abort(403)

@bot.message_handler(commands=['start'])
def start(message):
    User.create_user(str(message.chat.id))
    Cart.get_or_create_cart(str(message.chat.id))
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
    user_id = call.from_user.id

    cart = Cart.get_cart(str(user_id))

    cart.add_product_to_cart(product_id=prod_id)

    bot.answer_callback_query(call.id, "Добавлено в корзину", show_alert=True)


@bot.callback_query_handler(func=lambda call: call.data == START_KB['cart'])
def get_root_category(call):
    print('get_Cart')

    bot.show_cart(str(call.from_user.id))


@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'del')
def del_prod_from_cart(call):
    print('inline_handler Del product from cart')
    prod_id = call.data.split('_')[1]

    bot.del_product_from_cart(prod_id, call.id, str(call.from_user.id))

@bot.message_handler(func=lambda message: message.text == 'Оформить заказ')
def checkout(message):

    bot.checkout_step_1(str(message.from_user.id))


@bot.message_handler(func=lambda message: User.get_step(str(message.chat.id)) == 1)
def save_name_go_step_2(message):

    bot.checkout_step_2(str(message.from_user.id), message.text)

@bot.message_handler(func=lambda message: User.get_step(str(message.chat.id)) == 2)
def save_name_go_step_3(message):

    bot.checkout_step_3(str(message.from_user.id), message.text)

@bot.message_handler(func=lambda message: User.get_step(str(message.chat.id)) == 3)
def save_name_go_step_4(message):

    bot.checkout_step_4(str(message.from_user.id), message.text)

@bot.callback_query_handler(func=lambda call: call.data == START_KB['story'])
def story_order(call):

    bot.story_order(str(call.from_user.id))

@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'story')
def show_archive_order(call):
    id_cart = call.data.split('_')[1]


    bot.show_archive_cart(str(call.from_user.id), id_cart)







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
    utils.start_bot()