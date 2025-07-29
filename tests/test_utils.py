import os.path

from src.category import Category
from src.product import Product
from src.utils import create_objects_from_json, read_json


def test_read_json(json_data: list[dict]) -> None:
    path_json = os.path.abspath("data/products.json")
    assert read_json(path_json) == json_data


def test_read_json_non_existent_file() -> None:
    new_path_json = os.path.abspath("data/new_products.json")
    assert read_json(new_path_json) == []


def test_read_json_incorrect_data():
    path_temp_json = os.path.abspath("data/temp_products")
    with open(path_temp_json, "w", encoding="utf-8") as temp_file:
        temp_file.write("[Смартфоны и Телевизоры]")
    assert read_json(path_temp_json) == []
    os.remove(path_temp_json)


def test_create_objects_from_json(json_data: list[dict]) -> None:
    categories = create_objects_from_json(json_data)
    assert isinstance(categories, list)
    assert len(categories) == 2

    category_1 = categories[0]
    assert isinstance(category_1, Category)
    assert category_1.name == "Смартфоны"
    assert (
        category_1.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert isinstance(category_1.products_list, list)
    assert len(category_1.products_list) == 3

    product_1 = category_1.products_list[0]
    assert isinstance(product_1, Product)
    assert product_1.name == "Samsung Galaxy C23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5

    product_2 = category_1.products_list[1]
    assert isinstance(product_2, Product)
    assert product_2.name == "Iphone 15"
    assert product_2.description == "512GB, Gray space"
    assert product_2.price == 210000.0
    assert product_2.quantity == 8

    product_3 = category_1.products_list[2]
    assert isinstance(product_3, Product)
    assert product_3.name == "Xiaomi Redmi Note 11"
    assert product_3.description == "1024GB, Синий"
    assert product_3.price == 31000.0
    assert product_3.quantity == 14

    category_2 = categories[1]
    assert isinstance(category_2, Category)
    assert category_2.name == "Телевизоры"
    assert (
        category_2.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert isinstance(category_2.products_list, list)
    assert len(category_2.products_list) == 1

    product_4 = category_2.products_list[0]
    assert isinstance(product_4, Product)
    assert product_4.name == '55" QLED 4K'
    assert product_4.description == "Фоновая подсветка"
    assert product_4.price == 123000.0
    assert product_4.quantity == 7
