from src.product import Product
from src.category import Category


def test_first_product_init(first_product):
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5


def test_second_product_init(second_product):
    assert second_product.name == "Iphone 15"
    assert second_product.description == "512GB, Gray space"
    assert second_product.price == 210000.0
    assert second_product.quantity == 8


def test_third_product_init(third_product):
    assert third_product.name == "Xiaomi Redmi Note 11"
    assert third_product.description == "1024GB, Синий"
    assert third_product.price == 31000.0
    assert third_product.quantity == 14


def test_fourth_product_init(fourth_product):
    assert fourth_product.name == '55" QLED 4K'
    assert fourth_product.description == "Фоновая подсветка"
    assert fourth_product.price == 123000.0
    assert fourth_product.quantity == 7


def test_product_count():
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product(name="Товар A", description="Описание A", price=10.0, quantity=5)
    p2 = Product(name="Товар B", description="Описание B", price=20.0, quantity=3)

    Category(name="Кат1", description="Описание 1", products=[p1, p2])  # +2 товара
    Category(name="Кат2", description="Описание 2", products=[p1])  # +1 товар

    assert Category.product_count == 3
