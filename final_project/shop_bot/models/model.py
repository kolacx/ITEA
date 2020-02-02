from mongoengine import *
connect('shop')


class User(Document):
    telegram_id = StringField(max_length=32, required=True)
    username = StringField(max_length=128)
    fullname = StringField(max_length=256)
    phone_number = StringField(max_length=20)
    email = EmailField()

class Cart(Document):
    user = ReferenceField(User)
    is_archived = BooleanField(default=False)

    def get_cart(self):
        return CartProduct.objects.filter(cart=self)

    # TODO 
    # Overthink
    # def get_sum(self):
    #     return CartProduct.objects.filter(cart=self).sum()


class CartProduct(Document):
    cart = ReferenceField(Cart)
    product = ReferenceField('Product')


class Attributes(EmbeddedDocument):
    height = FloatField()
    weight = FloatField()
    width = FloatField()


class Category(Document):
    title = StringField(max_length=255, min_length=1, required=True, unique=True)
    description = StringField(max_length=4096)
    parent = ReferenceField('self')
    is_root = BooleanField(default=False)
    subcategories = ListField(ReferenceField('self'))

    def is_parent(self):
        return bool(self.parent)

    def add_subcategory(self, cat_obj):
        cat_obj.parent = self
        cat_obj.save()

        self.subcategories.append(cat_obj)
        self.save()

    @classmethod
    def create(cls, **kwargs):
        kwargs['subcategories'] = []

        if kwargs.get('parent') == True:
            kwargs['is_root'] == False

        Product(**kwargs).save()

    def get_products(self):
        return Product.objects.filter(
                category=self
            )


class Product(Document):
    title = StringField(max_length=255, min_length=1, required=True)
    article = StringField(max_length=32, required=True)
    description = StringField(max_length=4096)
    price = IntField(min_value=1, required=True)
    in_stock = IntField(min_value=0, default=0) # Kolichestvo
    discount_price = IntField(min_value=1)
    attributes = EmbeddedDocumentField(Attributes)
    extra_data = StringField(max_length=4096)
    category = ReferenceField(Category, required=True)

    def get_price(self):
        return self.price if not self.discount_price else self.discount_price


class Texts(Document):
    TEXT_TYPES = (
            ('Greeting', 'Greeting'),
            ('News', 'News'),
        )

    text_type = StringField(choices=TEXT_TYPES)
    body = StringField(max_length=2048)