from bot import TGbot
from config import TOKEN
from models.model import Category, Product, Texts
from keyboards import START_KB
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

bot = TGbot(token=TOKEN)

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

# @bot.message_handler(func=lambda message: message.text == START_KB['categories'])
# def show_news(message):
#     category = Category.objects.filter(
#             is_root=True
#         )

#     for cat in category:
#         mes = (f'{cat.title} \n' 
#                 f'{cat.description}')

#         kb = InlineKeyboardMarkup(row_width=1)
#         buttons = [InlineKeyboardButton(callback_data=cat.title, text='Перейти в категорию')]
#         kb.add(*buttons)

#         bot.send_message(message.chat.id, mes, reply_markup=kb)

@bot.message_handler(func=lambda message: message.text == START_KB['categories'])
def category(message):
    category = Category.objects.filter(
            is_root=True
        )

    kb = InlineKeyboardMarkup()
    buttons = [
        InlineKeyboardButton(text=cat.title, callback_data=str(cat.id)) for cat in category
    ]

    kb.add(*buttons)

    bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=kb)

@bot.callback_query_handler(func=lambda call: True)
def get_cat_or_products(call):

    """

    Приходит ИД категории, получаем обьект этой категории:
    1) Если обьект не имеет предков выводим продукты
    2) Если обьект имеет предков , выводим етих предков
    """
    # print(call.data)

    # bot.send_message(call.message.chat.id, call.data)

    kb = InlineKeyboardMarkup()

    category = Category.objects.get(id=call.data)

    if category.subcategories:
        # Наполнения еще одной клавиатуры с категориями
        buttons = [
            InlineKeyboardButton(text=cat.title, callback_data=str(cat.id)) for cat in category.subcategories
        ]

        kb.add(*buttons)
        bot.edit_message_text(category.title,
                                message_id=call.message.message_id, 
                                chat_id=call.message.chat.id,  
                                reply_markup=kb)
        # bot.send_message(call.message.chat.id, category.title, reply_markup=kb)

    else:
        for product in category.get_product():
            mes = (f'{product.title} \n' 
                    f'{product.description}') 

            buttons = [InlineKeyboardButton(callback_data=str(product.id), text='Посмотреть товар')]
            kb.add(*buttons)

            # send_photo - Сюдой все передать

            bot.send_message(message.chat.id, mes, reply_markup=kb)


        # Выводим продукты етой
        # buttons = [
        #     InlineKeyboardButton(text=product.title, callback_data=str(product.id)) 
        #     for product in category.get_product() 
        # ]
        

    
    




if __name__ == '__main__':
    bot.polling()