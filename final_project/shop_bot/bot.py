from telebot import TeleBot
from models.model import Category, Texts, Cart, Product, User
from keyboards import START_KB
from telebot import types

class TGbot(TeleBot):

    def __init__(self, token, *args):
        super().__init__(token, *args)

    def send_start(self, chat_id, force_send=True):
        txt = Texts.objects.filter(
            text_type='Greeting'
            ).get()

        

        kb = types.InlineKeyboardMarkup()
        buttons = [types.InlineKeyboardButton(button_name, callback_data=button_name) for button_name in START_KB.values()]
        kb.add(*buttons)

        if not force_send:
            return kb

        self.send_message(chat_id, txt.body, reply_markup=kb)


    def root_categories(self, user_id, text, callback_lookup='category', force_send=True):
        category = Category.objects.filter(
                is_root=True
            )

        kb = types.InlineKeyboardMarkup()
        buttons = [
            types.InlineKeyboardButton(text=cat.title, callback_data=f'{callback_lookup}_{str(cat.id)}') for cat in category
        ]

        kb.add(*buttons)

        if not force_send:
            return kb
        
        self.send_message(user_id, text, reply_markup=kb)


    def subcategories_or_products(self, 
            category_id, 
            message_id,
            user_id=None, 
            text=None,
            category_loockup='category', 
            product_loockup='product',
            force_send=True):

        if not(all([user_id, text])) and force_send:
            raise Exception('Force send cannot be used without user_id or text')

        # Берем категорию
        category = Category.objects.get(id=category_id)

        kb = types.InlineKeyboardMarkup(row_width=2)

        # Проверяем есть ли у категории Под категории
        if category.subcategories:

            # Проверяем все подкатегории нашей Категории
            for cat in category.subcategories:

                # Если у нашей под категории есть еще подкатегории.
                # Создаем Inline кнопки в сообщении
                if cat.subcategories:
                    buttons = [
                        types.InlineKeyboardButton(text=cat.title, callback_data=f'{category_loockup}_{cat.id}')  for cat in category.subcategories
                    ]

                # Иначе будем отправлять кнопки с switch_inline_query_current_chat
                else:
                    buttons = [
                        types.InlineKeyboardButton(text=cat.title, switch_inline_query_current_chat=f'{category_loockup}_{cat.id}') for cat in category.subcategories
                    ]

            # Добавляем все созданные кнопки
            kb.add(*buttons)

            self.edit_message_text(category.title, message_id=message_id, chat_id=user_id, reply_markup=kb)

        else:
            results = []

            for product in category.get_products():
                
                url_img = 'https://s.ftcdn.net/v2013/pics/all/curated/RKyaEDwp8J7JKeZWQPuOVWvkUjGQfpCx_cover_580.jpg'

                kb = types.InlineKeyboardMarkup()

                button = types.InlineKeyboardButton(text='Добавить в корзину', callback_data=f'{product_loockup}_{product.id}')

                kb.add(button)
                result1 = types.InlineQueryResultArticle(
                            id=str(product.id),
                            title=product.title,
                            description=product.description,
                            thumb_url=url_img,
                            reply_markup=kb,

                            input_message_content=types.InputTextMessageContent(
                                parse_mode='HTML',
                                disable_web_page_preview=False,
                                message_text=f"{product.title} \n{product.description} <a href='{url_img}'>&#8204</a>"
                            )


                        )
                results.append(result1)

            self.answer_inline_query(message_id, results, cache_time=0)


    def show_cart(self, user_id, text, product_loockup='product', force_send=True):

        user = User.get_user(user_id)
        cart = Cart.get_cart(user_id)

        cart_product = cart.get_cart_products()

        kb = types.InlineKeyboardMarkup(row_width=2)

        buttons = [
            types.InlineKeyboardButton(text=pr.title, callback_data=f'{product_loockup}_{pr.id}')  for pr in cart_product
        ]

        kb.add(*buttons)

        if not force_send:
            return kb

        self.send_message(user_id, text, reply_markup=kb)