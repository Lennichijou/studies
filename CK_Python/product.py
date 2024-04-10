class NegativeCostError(Exception):
    def __init__(self, name, cost, width, height, length):
        self.height = height
        self.length = length
        self.width = width
        self.name = name
        self.cost = cost

    def __str__(self):
        return f"NegativeCostError: цена не может быть отрицательной."


class Product:
    # Конструктор
    def __init__(self, name: str, cost: float, width: int, height: int, length: int):
        self.__name = name
        self.__width = width
        self.__height = height
        self.__length = length
        if cost > 0:
            self.__cost = cost
        else:
            raise NegativeCostError(self, cost, width, height, length)

    @property
    def cost(self):
        return self.__cost

    @property
    def name(self):
        return self.__name

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    # Финальная цена с учётом скидки
    def final_cost(self, discount: int) -> float:
        f_cost = self.__cost * (1 - discount / 100)
        if f_cost >= 0.01:
            return round(f_cost, 2)
        else:
            return 0.01

    # Количество товара в коробке
    def product_count(self, box_length: int, box_width: int, box_height: int) -> int:
        return int((box_length * box_width * box_height) / (self.__height * self.__length * self.__width))

    # Перегрузка оператора +
    def __add__(self, other):
        return self.__cost + other.__cost

    def __str__(self):
        return f"Название: {self.__name}\nГабариты: {self.__width}*{self.__length}*{self.__height}\nЦена: {self.__cost} руб."

    def display_info(self):
        print(self.__str__())
