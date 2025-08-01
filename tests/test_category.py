import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.product_iterator import ProductIterator
from src.smartphone import Smartphone


def test_category_init(first_category: Category, second_category: Category) -> None:
    assert first_category.name == "Смартфоны"
    assert (
        first_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(first_category.products_list) == 3

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 4
    assert second_category.product_count == 4


def test_category_products_property(first_category: Category) -> None:
    assert first_category.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_add_product(first_category: Category) -> None:
    assert len(first_category.products_list) == 3
    new_product = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    first_category.add_product(new_product)
    assert len(first_category.products_list) == 4


def test_add_product_error(first_category: Category) -> None:
    with pytest.raises(TypeError):
        first_category.add_product(1)


def test_add_product_smartphone(
    first_category: Category, smartphone1: Smartphone
) -> None:
    first_category.add_product(smartphone1)
    assert first_category.products_list[-1].name == "Samsung Galaxy S23 Ultra"


def test_add_product_grass(first_category: Category, grass1: LawnGrass) -> None:
    first_category.add_product(grass1)
    assert first_category.products_list[-1].name == "Газонная трава"


def test_category_str(first_category: Category) -> None:
    assert str(first_category) == "Смартфоны, количество продуктов: 27 шт."


def test_product_iterator(product_iterator: ProductIterator) -> None:
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(product_iterator).name == "Iphone 15"
    assert next(product_iterator).name == "Xiaomi Redmi Note 11"
    with pytest.raises(StopIteration):
        next(product_iterator)
