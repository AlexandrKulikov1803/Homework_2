from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @classmethod
    @abstractmethod  # pragma: no cover
    def new_product(cls, *args, **kwargs):
        pass

    @abstractmethod  # pragma: no cover
    def __str__(self):
        pass

    @abstractmethod  # pragma: no cover
    def __add__(self, other):
        pass

    @property
    @abstractmethod  # pragma: no cover
    def price(self):
        pass

    @price.setter
    @abstractmethod  # pragma: no cover
    def price(self, new_price):
        pass
