from src.product import Product
from src.category import Category


def test_first_category_init(first_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == (
        "Смартфоны, как средство не только коммуникации, но и получения "
        "дополнительных функций для удобства жизни"
    )
    assert len(first_category.products.split("\n")) == 3
    assert isinstance(first_category.products, str)


def test_second_category_init(second_category):
    assert second_category.name == "Телевизоры"
    assert second_category.description == (
        "Современный телевизор, который позволяет наслаждаться просмотром, "
        "станет вашим другом и помощником"
    )
    assert len(second_category.products.split("\n")) == 1



def test_category_count():
    Category.category_count = 0
    Category.product_count = 0

    Category(name="Кат1", description="Описание 1", products=[])
    Category(name="Кат2", description="Описание 2", products=[])

    assert Category.category_count == 2

def test_category_count_with_products():
    """product_count учитывает товары, переданные при создании."""
    Category.category_count = 0
    Category.product_count = 0

    category = Category(
        "Тест", "Описание",
        [Product("А", "оп", 10.0, 1), Product("Б", "оп", 20.0, 2)]
    )

    assert Category.category_count == 1
    assert Category.product_count == 2


def test_add_product_increases_product_count():
    """add_product добавляет товар и увеличивает product_count на 1."""
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Тест", "Описание", [])
    category.add_product(Product("Чайник", "Электрический", 2000.0, 5))

    assert Category.product_count == 1


def test_products_getter_returns_string():
    """Геттер products возвращает строку, а не список."""
    category = Category("Тест", "Описание", [])
    assert isinstance(category.products, str)


def test_products_getter_empty_category():
    """Пустая категория возвращает пустую строку."""
    category = Category("Тест", "Описание", [])
    assert category.products == ""


def test_products_getter_single_product():
    """Геттер форматирует один товар в нужном виде."""
    category = Category("Тест", "Описание", [])
    category.add_product(Product("Кофе", "Зерновой", 80.0, 15))

    assert category.products == "Кофе, 80.0 руб. Остаток: 15 шт."


def test_products_getter_joins_multiple_products():
    """Несколько товаров соединяются в одну строку через \n."""
    category = Category("Тест", "Описание", [])
    category.add_product(Product("Чайник", "Оп", 2000.0, 5))
    category.add_product(Product("Кофе", "Оп", 80.0, 15))

    expected = "Чайник, 2000.0 руб. Остаток: 5 шт.\nКофе, 80.0 руб. Остаток: 15 шт."
    assert category.products == expected
    assert len(category.products.split("\n")) == 2


def test_add_product_then_products_string():
    """После add_product товар появляется в строке геттера."""
    category = Category("Тест", "Описание", [])
    product = Product("Телевизор", "QLED", 123000.0, 7)

    category.add_product(product)

    assert category.products == "Телевизор, 123000.0 руб. Остаток: 7 шт."
