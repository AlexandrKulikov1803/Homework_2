from src.product import Product


class LawnGrass(Product):
    """Класс для хранения продукта - трава газонная"""

    country: str
    germination_period: str
    color: str

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        """Конструктор для продукта - трава газонная"""

        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """Метод для подсчёта суммарной стоимости продуктов одного класса с учётом количества"""

        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError
