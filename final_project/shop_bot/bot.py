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
            print('KB')
            return kb
        
        print('Message')
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

        category = Category.objects.get(id=category_id)

        kb = types.InlineKeyboardMarkup()

        if category.subcategories:
            # Наполнения еще одной клавиатуры с категориями
            

            buttons = [
                types.InlineKeyboardButton(text=cat.title, callback_data=f'{category_loockup}_{cat.id}') for cat in category.subcategories
            ]

            kb.add(*buttons)
            self.edit_message_text(category.title,
                                    message_id=message_id, 
                                    chat_id=user_id,  
                                    reply_markup=kb)
            # self.send_message(call.message.chat.id, category.title, reply_markup=kb)

        else:

            for product in category.get_products():
                mes = (f'{product.title} \n' 
                        f'{product.description}') 

                buttons = [types.InlineKeyboardButton(callback_data=f'{product_loockup}_{product.id}', text='Посмотреть товар')]
                kb.add(*buttons)

                # send_photo - Сюдой все передать

                self.send_message(user_id, mes, reply_markup=kb)

        # kb = types.InlineKeyboardMarkup()
        # kb.add(*buttons)

        # if not force_send:
        #     return kb

        # self.send_message(user_id, text, reply_markup=kb)