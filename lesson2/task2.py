class Market:

    total = 0

    def __init__(self, name, sale_product):
        self._name = name
        self._sale_product = sale_product
        Market.total += sale_product

    def set_product(self, add_product):
        self._sale_product += add_product
        Market.total += add_product


market1 = Market('ATB', 200)

market1.set_product(20)

print(Market.total)

market2 = Market('Silpo', 400)

market2.set_product(20)

print(Market.total)