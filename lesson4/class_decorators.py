class Shop:

    _total_sale = 0

    def __init__(self, name, sales):
        self._name = name
        self._sales = sales
        Shop._total_sale += sales

    @classmethod
    def get_total_sales(cls):
        return cls._total_sale

    @staticmethod
    def get_total_static_sales():
        return Shop._total_sale

    def __call__(self):
        print(f'hi iam obj class {self.__class__.__name__}')


# Shop.get_total_sales()

shop_obj = Shop('ATB', 400)

shop_obj()

class Decorator:

    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        print(f'Decorationg {self._func.__name__}')
        self._func()

@Decorator  
def my_func():
    pass

my_func()