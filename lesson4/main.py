print('hi')

a = 'test'

type(type(str))

class My:
    pass

# print(type(My))


def my_func():
    pass


a = type('MyClass', (), {'attr1': 1,
                         'attr2': 2,
                         'func_1': my_func})

# Равносильно созданию обычного класа

print(a)
print(dir(a))

print(a.attr1)
print(a.attr2)

# Metoclass

