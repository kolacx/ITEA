from models.model import Texts, Category

# cat = Category.objects.all()

# for i in cat:
#     print(i.title, i.description, i.parent, i.is_root, i.subcategories)
    # i.delete()


def add_category(**kwargs):
    try:
        Category(**kwargs).save()
        print('Category add')
    except Exception as e:
        print(e)
        pass

for i in range(10):
    new_cat = {
        'title':f'Category{i}',
        'description':f'Description of category{i}'
    }

    add_category(**new_cat)
    print('fin')