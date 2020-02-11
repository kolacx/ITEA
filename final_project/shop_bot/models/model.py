from mongoengine import *
db = connect('shop')


class User(Document):

    STATES = (
            ('products', 'products'),
            ('categories', 'categories'),
        )

    telegram_id = StringField(max_length=32, required=True, unique=True)
    username = StringField(max_length=128)
    fullname = StringField(max_length=256)
    phone_number = StringField(max_length=20)
    email = EmailField()
    state = StringField(choises=STATES)

class Cart(Document):
    user = ReferenceField(User)
    is_archived = BooleanField(default=False)

    @classmethod
    def get_or_create_cart(cls, user_id):
        user = User.objects.get(id=user_id)
        cart = cls.objects.get(user, is_archived=False) # pri start sozdat Cart

        if not cart:
            cart = cls.objects.create(user=user)

        return cart

    def get_cart_products(self):
        return CartProduct.objects.filter(cart=self)


    def add_product_to_cart(self, product_id):
        CartProduct.objects.create(
            cart=self,
            product=Product.get_product(id=product_id)
        )

    def delete_product_from_cart(self, product):
        CartProduct.objects.filter(
            cart=self,
            product=product
        ).first().delete()


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
    title = StringField(max_length=255, min_length=1, required=True)
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

        return cls(**kwargs).save()
        

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
    image = FileField(required=True)

    def get_price(self):
        return self.price if not self.discount_price else self.discount_price

    @classmethod
    def get_product(cls, **kwargs):
        return cls.objects.get(kwargs)


class Texts(Document):
    TEXT_TYPES = (
            ('Greeting', 'Greeting'),
            ('News', 'News'),
        )

    text_type = StringField(choices=TEXT_TYPES)
    body = StringField(max_length=2048)


if __name__ == '__main__':
    print('model')

    ### Creation
    # category_dict = {
    #     'title': 'category1',
    #     'description': 'category1 description',
    #     'is_root': True, 
    # }

    # root_cat = Category.create(**category_dict)

    # for i in range(5):
    #     category_dict = {
    #         'title': f'Sub_category{i}',
    #         'description': f'Sub_category{i} description',
    #     }
    #     sub_cat = Category(**category_dict)
    #     root_cat.add_subcategory(sub_cat)

    ### END

    # cats = Category.objects.filter(is_root=True)

    # for cat in cats:
    #     print(cat)

    #     if cat.subcategories:
    #         for sub in cat.subcategories:
    #             print(f'Parent is {sub.parent}')
    #             print(f'sub cat {sub}')

    # ITEMS FREQUENCIES

    # user = User.objects.create(telegram_id='12345')

    # cart = Cart.objects.create(user=user)

    # for i in range(10):

    #     prod = {
    #         'title': f'title{i}',
    #         'article': f'article{i}',
    #         'category': Category.objects.first(),
    #         'price': 10 * i + 1
    #     }

    #     created_product = Product.objects.create(**prod)
    #     cart.add_product_to_cart(created_product)

    # cart = Cart.objects.first()
    # print(cart.get_cart())

    # print(cart.get_cart().item_frequencies('product')) """ Prod i kolichestvo """