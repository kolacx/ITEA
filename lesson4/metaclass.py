class FromMeta:
    
    def hello(self):
        print('hello')

class UpperCaseMetaclass(type):

    def __new__(cls, name, base, attrs):
        # print(name, base, attrs)

        for i in range(5):
            base = (FromMeta,)
            attrs.update({'var_' + str(i): i})

        return super().__new__(cls, name, base, attrs)


class MiddleWare(metaclass=UpperCaseMetaclass):
    pass

class Inherit():
    pass


class MyClass(Inherit, MiddleWare):

    _attribute_of_class = 'Attr'

    def __init__(self, x, y):
        self._x = x
        self._y = y


MyClass(1, 2)
print(dir(MyClass))

MyClass(1, 2).hello()

# print(MyClass.__bases__) # otmena