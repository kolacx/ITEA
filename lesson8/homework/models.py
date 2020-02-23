from mongoengine import *
db = connect('shop2')

class Category(Document):
    title = StringField(max_length=255, min_length=1, required=True)
    description = StringField(max_length=4096)


class Product(Document):
	category = ReferenceField(Category, required=True)
	title = StringField(max_length=255, min_length=1, required=True)
	in_sale = BooleanField(default=True)
	price = IntField(min_value=1, required=True)
	in_stock = IntField(min_value=0, default=0)