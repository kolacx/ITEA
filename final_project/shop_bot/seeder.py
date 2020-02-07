from models.model import Texts, Category, db, User, Cart, Product

from datetime import datetime
dt = datetime.now()


# db.drop_database('shop') 

## Creation Создаем 5 категорий и под каждую из них 1 подкатегорию

Texts(text_type='Greeting',
    body='Какойто текст приведствия').save()

for i in range(5):

    category_dict = {
        'title': f'category{i}',
        'description': f'category{i} description',
        'is_root': True, 
    }

    root_cat = Category.create(**category_dict)
    
    sub_category_dict = {
        'title': f'Sub_category{i}',
        'description': f'Sub_category{i} description',
    }

    sub_cat = Category(**sub_category_dict)
    root_cat.add_subcategory(sub_cat)

    for i in range(20):
        product_dict = {
            'title': f'Название {i}',
            'article': str(dt.microsecond),
            'description': f'писание товара {i}',
            'price': 10 * i + 1,
            'in_stock': 0,
            'discount_price': i + 1,
            'extra_data': f'Extra Data {i}',
            'category': sub_cat
        }

        pr = Product.objects.create(**product_dict)

        with open('image.jpg', 'rb') as image_file:
            print(image_file)
            pr.image.put(image_file, content_type='image/jpg')
            pr.save()

# prod = Product.objects.all()

# for i in prod:
#     print(i.image)

txt = Texts.objects.all()

for i in txt:
    print(i)


cat = Category.objects.all()

for i in cat:
    print(i)