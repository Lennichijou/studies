from product import Product


class HouseholdGoods(Product):
    def __init__(self, name, cost, weight, height, length):
        Product.__init__(self, name, cost, weight, height, length)