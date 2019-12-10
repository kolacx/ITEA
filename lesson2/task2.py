class Market:

    total = 0

    def __init__(self, name, sale_product):
        self._name = name
        self._sale_product = sale_product
        self.total += sale_product

    def set_product(self, add_product):
        self._sale_product += add_product

    def show_total_sale(self):
        print(self.total)

market1 = Market('ATB', 200)

print(market1._name)
print(market1._sale_product)

market1.set_product(20)

print(market1._sale_product)

Market.show_total_sale(market1)