from src.product import Product


class Category:
    name: str
    description: str
    __products: list
    total_quantity: int

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        self.total_quantity = 0

        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        for product in self.__products:
            self.total_quantity += product.quantity
        return f"{self.name}, количество продуктов: {self.total_quantity} шт."

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    @property
    def products_list(self):
        return self.__products
