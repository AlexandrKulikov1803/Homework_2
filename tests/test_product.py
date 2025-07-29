from src.product import Product


def test_product_init(product1: Product) -> None:
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_new_product() -> None:
    Product.all_products = []
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert Product.all_products[0].name == "Samsung Galaxy S23 Ultra"
    assert Product.all_products[0].description == "256GB, Серый цвет, 200MP камера"
    assert Product.all_products[0].price == 180000
    assert Product.all_products[0].quantity == 5
    assert len(Product.all_products) == 1

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
    assert len(Product.all_products) == 1

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
    assert len(Product.all_products) == 2


def test_product_str(product1: Product) -> None:
    assert str(product1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_add(product1: Product, product2: Product) -> None:
    assert product1 + product2 == 2580000.0
