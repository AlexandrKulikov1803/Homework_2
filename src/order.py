from src.product import Product


class Order:
    """Класс заказа одного товара"""

    product: Product
    quantity: int

    def __init__(self, product, quantity):
        """Конструктор для заказа"""

        self.product = product
        self.quantity = quantity

    def get_total_cost(self):
        if isinstance(self.product, Product):
            return self.product.price * self.quantity
        else:
            raise TypeError

    def __str__(self):

        return (
            f"Выбран продукт: {self.product.name}, количество: {self.quantity} шт.\n"
            f"Общая стоимость: {self.get_total_cost()}"
        )
