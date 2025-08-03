from src.exceptions import ZeroQuantity
from src.product import Product


class Category:
    """Класс для хранения категории"""

    name: str
    description: str
    __products: list
    total_quantity: int

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        """Конструктор для категории"""

        self.name = name
        self.description = description
        self.__products = products if products else []
        self.total_quantity = 0

        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        """Метод для отображения информации пользователю о категории"""

        for product in self.__products:
            self.total_quantity += product.quantity
        return f"{self.name}, количество продуктов: {self.total_quantity} шт."

    def add_product(self, product):
        """Метод для добавления продукта в категорию"""

        if isinstance(product, Product):
            try:
                if product.quantity <= 0:
                    raise ZeroQuantity(
                        "Товар с нулевым количеством не может быть добавлен"
                    )
            except ZeroQuantity as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.product_count += 1
                print("Задача добавлена успешно")
            finally:
                print("Обработка добавления задачи завершена")
        else:
            raise TypeError

    @property
    def products(self):
        """Метод для отображения информации пользователю о продуктах из категории"""

        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    @property
    def products_list(self):
        """Метод возвращает список продуктов из категории"""

        return self.__products

    def middle_price(self):
        try:
            return round(
                sum([product.price for product in self.__products])
                / len(self.__products),
                2,
            )
        except ZeroDivisionError:
            return 0
