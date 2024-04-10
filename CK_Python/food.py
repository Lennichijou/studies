from product import Product


class NoCalError(Exception):
    def __init__(self, name, cost, width, height, length, calories):
        self.calories = calories

    def __str__(self):
        return f"NoCalError: Продукт не может обладать энергетической ценностью меньшей/равной нулю."


class Food(Product):
    def __init__(self, name, cost, weight, height, length, calories):
        Product.__init__(self, name, cost, weight, height, length)
        if calories > 0:
            self.__calories = calories
        else:
            raise NoCalError(self, cost, weight, height, length, calories)

    @property
    def calories(self):
        return self.__calories

    @calories.setter
    def calories(self, calories):
        if calories > 0:
            self.__calories = calories
        else:
            raise NoCalError(self)

    def display_info(self):
        Product.display_info(self)
        print(f"Энергетическая ценность: {self.__calories} ккал")
