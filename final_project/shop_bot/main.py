from bot import TGbot
from config import TOKEN
from models.model import Category, Product, Texts
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
def get_root_category(call):
    print('Add to Card')
    prod_id = call.data.split('_')[1]

    bot.add_to_card(prod_id, call.from_user.id)



if __name__ == '__main__':
    bot.polling()