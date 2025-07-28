from unittest.mock import patch

from src.classes import Category, Product


def test_product_init(product: Product) -> None:
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


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


def test_category_products_property(first_category):
    assert first_category.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_add_product(first_category):
    assert len(first_category.products_list) == 3
    new_product = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    first_category.add_product(new_product)
    assert len(first_category.products_list) == 4


def test_product_price_setter(capsys, product):
    product.price = -1000
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    product.price = 200000
    assert product.price == 200000

    with patch("src.classes.input", return_value="y"):
        product.price = 150000
        assert product.price == 150000

    with patch("src.classes.input", return_value="n"):
        product.price = 120000
        assert product.price == 150000


def test_new_product():
    assert Product.all_products[0].name == "Samsung Galaxy S23 Ultra"
    assert Product.all_products[0].description == "256GB, Серый цвет, 200MP камера"
    assert Product.all_products[0].price == 180000
    assert Product.all_products[0].quantity == 5
    assert len(Product.all_products) == 13

    Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 200000.0,
            "quantity": 6,
        }
    )
    assert Product.all_products[0].name == "Samsung Galaxy S23 Ultra"
    assert Product.all_products[0].description == "256GB, Серый цвет, 200MP камера"
    assert Product.all_products[0].price == 200000
    assert Product.all_products[0].quantity == 11
    assert len(Product.all_products) == 13

    Product.new_product(
        {
            "name": "Honor 20",
            "description": "256GB, Чёрный цвет, 150MP камера",
            "price": 32000.0,
            "quantity": 15,
        }
    )
    assert Product.all_products[-1].name == "Honor 20"
    assert Product.all_products[-1].description == "256GB, Чёрный цвет, 150MP камера"
    assert Product.all_products[-1].price == 32000
    assert Product.all_products[-1].quantity == 15
    assert len(Product.all_products) == 14
