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

                    # back = types.InlineKeyboardButton(text='Назад', callback_data=f'{category_loockup}_{category.id}')

                    # buttons.append(back)

                # Иначе будем отправлять кнопки с switch_inline_query_current_chat
                else:
                    buttons = [
                        types.InlineKeyboardButton(text=cat.title, switch_inline_query_current_chat=f'{category_loockup}_{cat.id}') for cat in category.subcategories
                    ]

                    # back = types.InlineKeyboardButton(text='Назад', callback_data=f'{category_loockup}_{category.id}')

                    # buttons.append(back)

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


    def show_cart(self, user_id, del_product_loockup='del'):

        user = User.get_user(user_id)
        cart = Cart.get_cart(user_id)

        cart_product = cart.get_cart_products()

        item_f = cart_product.item_frequencies('product')

        kb2 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        b2 = [types.KeyboardButton('Оформить заказ')]
        kb2.add(*b2)

        if item_f:

            for p_id, s in item_f.items():

                pr = Product.get_product(id=p_id)

                text = (f'{pr.title} \n{pr.description} \n{pr.category.title} \nCount: {s}')

                kb = types.InlineKeyboardMarkup(row_width=1)

                buttons = [
                    types.InlineKeyboardButton(text='Удалить товар с корзины', callback_data=f'{del_product_loockup}_{pr.id}')
                ]

                kb.add(*buttons)


                self.send_message(user_id, text, reply_markup=kb)

            self.send_message(user_id, 'Чтобы купить нажмите на кнопку "Оформить заказ"', reply_markup=kb2)
        else:

            self.send_message(user_id, 'Ваша корзина пуста')

            


    def del_product_from_cart(self, prod_id, message_id, user_id):

        user = User.get_user(user_id)
        cart = Cart.get_cart(user_id)
        cart.delete_product_from_cart(prod_id)

        self.answer_callback_query(message_id, "Товар удален", show_alert=True)

        self.send_message(user_id, 'Ваша корзина')

        self.show_cart(user_id)

    def checkout_step_1(self, user_id):

        User.set_step_checkout(user_id, 1)

        self.send_message(user_id, 'Введите ваше Имя')

    def checkout_step_2(self, user_id, response_name):

        User.update_user(user_id, username=response_name)
        User.set_step_checkout(user_id, 2)

        self.send_message(user_id, 'Введите ваше Телефон (0631234567)')

    def checkout_step_3(self, user_id, response_phone):

        User.update_user(user_id, phone_number=response_phone)
        User.set_step_checkout(user_id, 3)

        self.send_message(user_id, 'Введите ваш Емейл')

    def checkout_step_4(self, user_id, response_email):

        User.update_user(user_id, email=response_email)
        User.set_step_checkout(user_id, 4)

        Cart.archive_cart(user_id)

        # For Test
        user = User.get_user(user_id)

        mes = (f'Вот что ты ввел \n'
                f'Name: {user.username} \n'
                f'Phone: {user.phone_number} \n'
                f'email: {user.email} \n'
                )

        self.send_message(user_id, 'Заказ оформлен. С вами свяжется наш Менеджер')
        self.send_message(user_id, mes)


    def story_order(self, user_id, story_order_lookup='story'):

        cart = Cart.get_archive_cart(user_id)

        if cart:

            kb = types.InlineKeyboardMarkup()
            buttons = [
                types.InlineKeyboardButton(text=f'Корзина {i}', callback_data=f'{story_order_lookup}_{str(c.id)}') for i, c in enumerate(cart)
            ]

            kb.add(*buttons)

            self.send_message(user_id, 'Ваша история заказов', reply_markup=kb)
        else:

            self.send_message(user_id, 'Ваша история заказов Пуста')


    def show_archive_cart(self, user_id, id_cart):

        cart = Cart.get_archive_cart_by_id(user_id, id_cart)
        cart_product = cart.get_cart_products()

        item_f = cart_product.item_frequencies('product')

        for p_id, s in item_f.items():

            pr = Product.get_product(id=p_id)

            text = (f'{pr.title} \n{pr.description} \n{pr.category.title} \nCount: {s}')

            self.send_message(user_id, text)