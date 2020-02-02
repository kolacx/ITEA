from mongoengine import *
connect('users')

class User(Document):
    telegram_id = StringField(max_length=32, required=True)
    username = StringField(max_length=128)
    phone_number = StringField(max_length=20)
    email = EmailField()