import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def first_product():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def second_product():
    return Product(
        name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8
    )


@pytest.fixture
def third_product():
    return Product(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=14,
    )


@pytest.fixture
def fourth_product():
    return Product(
        name='55" QLED 4K', description="Фоновая подсветка", price=123000.0, quantity=7
    )


# --- Фикстуры категорий ---
@pytest.fixture
def first_category(first_product, second_product, third_product):
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения "
        "дополнительных функций для удобства жизни",
        products=[first_product, second_product, third_product],
    )


@pytest.fixture
def second_category(fourth_product):
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, "
        "станет вашим другом и помощником",
        products=[fourth_product],
    )
