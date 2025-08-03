from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Класс для хранения продукта"""

    name: str
    description: str
    __price: float
    quantity: int
    all_products: list = []

    def __init__(self, name, description, price, quantity):
        """Конструктор для продукта"""

        self.name = name
        self.description = description
        self.__price = price
        if quantity > 0:
            self.quantity = quantity
            Product.all_products.append(self)
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        super().__init__()

    def __str__(self):
        """Метод для отображения информации пользователю о продукте"""

        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Метод для подсчёта суммарной стоимости продуктов одного класса с учётом количества"""

        if type(other) is self.__class__:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError

    @classmethod
    def new_product(cls, parameters):
        """Метод для создания нового продукта и проверки его в наличии"""

        for product in cls.all_products:
            if product.name == parameters.get("name"):
                product.quantity += parameters.get("quantity")
                product.price = max(product.price, parameters.get("price"))
                print(
                    f"При попытке добавления нового товара {product.name} обнаружен аналогичный товар. "
                    f"Количество товаров в указанной категории было увеличено. Новая позиция не добавлена."
                )
                return product
        return cls(**parameters)

    @property
    def price(self):
        """Метод, который возвращает цену продукта"""

        return self.__price

    @price.setter
    def price(self, new_price):
        """Метод для изменения цены продукта"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if new_price < self.__price:
                answer = input(
                    "Цена товара понижается. Нажмите y (yes), если согласны понизить цену "
                    "или n (no) для отмены действия соответственно:"
                )
                if answer == "y":
                    self.__price = new_price
            else:
                self.__price = new_price
