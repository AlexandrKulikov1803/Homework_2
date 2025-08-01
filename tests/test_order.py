import pytest

from src.lawn_grass import LawnGrass
from src.order import Order
from src.product import Product
from src.smartphone import Smartphone


def test_order_init(product2: Product) -> None:
    order1 = Order(product2, 3)
    assert order1.product.name == "Iphone 15"
    assert order1.product.description == "512GB, Gray space"
    assert order1.product.price == 210000.0
    assert order1.product.quantity == 8
    assert order1.quantity == 3


def test_order_str(
    product1: Product, smartphone1: Smartphone, grass1: LawnGrass
) -> None:
    assert str(Order(product1, 2)) == (
        "Выбран продукт: Samsung Galaxy S23 Ultra, количество: 2 шт.\n"
        "Общая стоимость: 360000.0"
    )
    assert (
        str(Order(smartphone1, 5))
        == "Выбран продукт: Samsung Galaxy S23 Ultra, количество: 5 шт.\nОбщая стоимость: 900000.0"
    )
    assert (
        str(Order(grass1, 4))
        == "Выбран продукт: Газонная трава, количество: 4 шт.\nОбщая стоимость: 2000.0"
    )


def test_get_total_cost(product1: Product, smartphone1: Smartphone, grass1: LawnGrass):
    assert Order(product1, 3).get_total_cost() == 540000.0
    assert Order(smartphone1, 3).get_total_cost() == 540000.0
    assert Order(grass1, 3).get_total_cost() == 1500.0
    with pytest.raises(TypeError):
        Order(10, 3).get_total_cost()
        Order("abc", 3).get_total_cost()
