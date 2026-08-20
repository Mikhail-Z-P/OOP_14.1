from src.product import Product
from src.category import Category


def test_first_category_init(first_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == (
        "Смартфоны, как средство не только коммуникации, но и получения "
        "дополнительных функций для удобства жизни"
    )
    assert len(first_category.products) == 3
    for product in first_category.products:
        assert isinstance(product, Product)


def test_second_category_init(second_category):
    assert second_category.name == "Телевизоры"
    assert second_category.description == (
        "Современный телевизор, который позволяет наслаждаться просмотром, "
        "станет вашим другом и помощником"
    )
    assert len(second_category.products) == 1


def test_category_count():
    Category.category_count = 0
    Category.product_count = 0

    Category(name="Кат1", description="Описание 1", products=[])
    Category(name="Кат2", description="Описание 2", products=[])

    assert Category.category_count == 2
