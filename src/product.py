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

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return self.price * self.quantity + other.price * other.quantity

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
