class Product:
    name: str
    description: str
    __price: float
    quantity: int
    all_products: list = []

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.all_products.append(self)

    @classmethod
    def new_product(cls, parameters):
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
        return self.__price

    @price.setter
    def price(self, new_price):
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


class Category:
    name: str
    description: str
    __products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

    @property
    def products_list(self):
        return self.__products
