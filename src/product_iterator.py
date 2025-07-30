class ProductIterator:
    """Итератор, возвращающий продукты из указанной категории"""

    def __init__(self, category):
        """Инициализирует итератор"""

        self.category = category
        self.index = 0

    def __iter__(self):
        """Возвращает итератор"""

        self.index = 0
        return self

    def __next__(self):
        """Возвращает следующий элемент списка"""

        if self.index < len(self.category.products_list):
            product = self.category.products_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
