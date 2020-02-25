from models.model import Texts, Category, db, User, Cart, Product

from datetime import datetime
dt = datetime.now()

# user = User.objects.all()

# for u in user:
#     print(u.telegram_id, u. username, u.phone_number, u.email, u.step)

db.drop_database('shop') 

# Creation Создаем 5 категорий и под каждую из них 1 подкатегорию

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

category = Category.objects.all()

for cat in category:
    for c in cat.subcategories:
        if not c.subcategories:
            for i in range(3):
                sub_sub_category_dict = {
                    'title': f'Sub_Sub_category{i}_{i}',
                    'description': f'Sub_Sub_category{i}_{i} description',
                }

                sub_sub_cat = Category(**sub_sub_category_dict)
                c.add_subcategory(sub_sub_cat)

                for i in range(20):
                    product_dict = {
                        'title': f'Название {i}',
                        'article': str(dt.microsecond),
                        'description': f'Описание товара {i}',
                        'price': 10 * i + 1,
                        'in_stock': 0,
                        'discount_price': i + 1,
                        'extra_data': f'Extra Data {i}',
                        'category': sub_sub_cat
                    }

                    pr = Product.objects.create(**product_dict)

                    with open('image.jpg', 'rb') as image_file:
                        print(image_file)
                        pr.image.put(image_file, content_type='image/jpg')
                        pr.save()
















# cart = Cart.objects.all()

# for c in cart:
# 	print(c.user.telegram_id)
# 	print(c)

# user = User.objects.all()

# for u in user:
# 	print(u)


# category = Category.objects.all()

# for cat in category:
#     print(f'Category title {cat.title}')
#     for c in cat.subcategories:
#         print(f'SubCategory title {c.title}')
#         for q in c.subcategories:
#             print(f'SubSubCategory title {q.title}')


#     if not cat.subcategories:
#         for i in range(3):
#             sub_sub_category_dict = {
#                 'title': f'Sub_Sub_category{i}_{i}',
#                 'description': f'Sub_Sub_category{i}_{i} description',
#             }

#             sub_sub_cat = Category(**sub_sub_category_dict)
#             cat.add_subcategory(sub_sub_cat)


