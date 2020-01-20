from mongoengine import *

class Products(Document):
    title = StringField(max_length=255)
    description = StringField(max_length=2048)
    price =DecimalField(min_value=0)

class User(Document):
    fullname = StringField(max_length=255, min_length=3)
    login = StringField(min_length=8, max_length=255, required=True)
    password = StringField(min_length=8, required=True)
    wishes = ListField(ReferenceField(Products))

    def __str__(self):
        return self.fullname

    def get_user_wishes(self):
        return self.wishes



if __name__ == '__main__':
    connect('my_db')
    # user = User.objects.create(
    #     fullname = 'Sasha23',
    #     login = 'sasha.cx423',
    #     password = 'qwerty123423',
    #     bill = 500.50,
    #     number = 124
    #     )

    # print(user.login, user.password, user.bill, user.number)

    # users = User.objects(fullname='Sasha')
    # print(users)

    # for user in users:
    #     print(user)

    # for user in User.objects:
    #     print(user.fullname)

    # user = User.objects.get(login='sasha.cx4')
    # user.number += 1

    # user.save()
    # print(user.number)

    # users = User.objects.filter(fullname__ne='Sasha')
    # print(users)


    # product_object = Products(
    #     title='iphone11', 
    #     description='This is phone', 
    #     price=1200).save()

    # product_object1 = Products(
    #     title='BMW',
    #     description='This is car',
    #     price=60000).save()

    # user = User(
    #     fullname='Paul Lense',
    #     login='mylogin1990',
    #     password='qwerty1234',
    #     wishes=[product_object, product_object1]

    #     ).save()

    # print(user.login)


    new_product = Products.objects.create(
        title='Mac',
        price=2000)

    user = User.objects.get()
    # print(user.wishes)

    # print(user.get_user_wishes())

    user.wishes.append(new_product)
    user.save()

    print(user.wishes)