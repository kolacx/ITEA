from models import Product, Category

# for i in range(10):

# 	category = {
# 		'title': f'Title{i}',
# 		'description': f'description{i}'
# 	}

# 	Category.objects.create(**category)

# all_category = Category.objects.all()

# for cat in all_category:

# 	for i in range(5):
# 		product = {
# 			'title': f'Название {i}',
# 			'price': 10 * i + 1,
# 			'in_stock': f'{i}',
# 			'category': cat,
# 			'in_sale': True
# 		}

# 		Product.objects.create(**product)



# cat = Category.objects.all()

# for i in cat:
# 	print(i.title)

pr = Product.objects.all()

for p in pr:
	print(p.title)