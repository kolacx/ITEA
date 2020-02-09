from telebot import TeleBot
from models.model import Category
from telebot import types

class TGbot(TeleBot):

    def __init__(self, token, *args):
        super().__init__(token, *args)

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
            print('STEP THIRD')
            results = []

            for product in category.get_products():
                # print('STEP ==========')
                print(product.id)
                kb = types.InlineKeyboardMarkup()

                button = types.InlineKeyboardButton(text='Добавить в корзину', callback_data=str(product.id))

                kb.add(button)
                result1 = types.InlineQueryResultArticle(
                            id=product.id,
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
            print(results)
            
            self.answer_inline_query(message_id, results, cache_time=0)




            # for product in category.get_products():
            #     mes = (f'{product.title} \n' 
            #             f'{product.description}') 

            #     buttons = [types.InlineKeyboardButton(callback_data=f'{product_loockup}_{product.id}', text='Посмотреть товар')]
            #     kb.add(*buttons)

            #     # send_photo - Сюдой все передать

            #     self.send_message(user_id, mes, reply_markup=kb)

        # kb = types.InlineKeyboardMarkup()
        # kb.add(*buttons)

        # if not force_send:
        #     return kb

        # self.send_message(user_id, text, reply_markup=kb)