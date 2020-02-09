from mongoengine import *
connect('users')

class Attributes(EmbeddedDocument):
    latitude = FloatField()
    longitude = FloatField()

class User(Document):
    telegram_id = StringField(max_length=32, required=True, unique=True)
    step = IntField(default=1, min_value=1, required=True)
    username = StringField(max_length=128)
    phone_number = StringField(max_length=20)
    location = EmbeddedDocumentField(Attributes)
    needs = StringField(max_length=1024)
    email = EmailField()