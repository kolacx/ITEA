class Cat:

    def __init__(self, name):
        self._name = name

    def meow(self):
        print('meow')

    def say_my_name(self):
        print(f'My name is {self._name}')

    def __add__(obj1, obj2):
        return Cat(obj1._name + obj2._name)


cat1 = Cat('1')
cat2 = Cat('2')

cat3 = cat1 + cat2

# cat3 = Cat(cat1._name + cat2._name)

cat3.say_my_name()






# print(Cat())

# def myfunc():
#     print('hi')


# def en_func(func1):
#     func1()

# en_func(myfunc)


# Polimorfizm

class A:
    def b(self):
        pass

class B(A):

    def b(self):
        super().b()
        print('do')

#Лямбда - онимная функция (нумбер то что передаем) range итерируемый обьект

def sqr(number):
    return namber ** 2

lambda number: number ** 2 

b = map(lambda number: number ** 2, range(100))

print(list(b))