from src.product import Product


class Smartphone(Product):
    """Класс для хранения продукта - смартфон"""

    efficiency: str
    model: str
    memory: int
    color: str

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        """Конструктор для продукта - смартфон"""

        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
