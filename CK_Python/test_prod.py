import pickle

from food import Food
from product import Product


class TestClass:
    def test_final_cost(self):
        assert Product.final_cost(Product("карамель", 0.01, 1, 1, 1), 10)

    def test_bat_file_write_and_read(self):
        products = [["шоколад", 25, 1, 2, 10], ["карамель", 10, 1, 1, 1], ["молоко", 12, 1, 1, 1]]
        filename = "data.bat"
        with open(filename, "wb") as file:
            pickle.dump(products, file)
        products = []
        with open(filename, "rb") as file:
            prod_input = pickle.load(file)
            for prod in prod_input:
                products.append(Product(prod[0], prod[1], prod[2], prod[3], prod[4]))
        for prod in products:
            assert prod

    def test_negative_cost_error(self):
        assert Product("карамель", 15, 1, 1, 1)

    def test_food_calories(self):
        food1 = Food("шоколад", 25, 1, 2, 10, 21)
        assert food1.calories

    def test_file_reading(self):
        file = open("data.txt", "r", encoding="utf-8")
        content = file.readlines()
        products2 = []
        for line in content:
            line = line.strip().split()
            products2.append(Product(line[0], float(line[1]), int(line[2]), int(line[3]), int(line[4])))
        for prod in products2:
            assert prod