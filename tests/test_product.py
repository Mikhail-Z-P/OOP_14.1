from abc import ABC

import pytest

from src.category import Category
from src.product import BaseProduct, LawnGrass, LogMixin, Product, Smartphone


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


def test_new_product_creates_product_from_dict():
    """new_product создаёт объект Product из словаря."""
    data = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
    product = Product.new_product(data)

    assert isinstance(product, Product)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_new_product_returns_instance():
    """new_product возвращает именно объект класса Product."""
    data = {"name": "Тест", "description": "оп", "price": 100.0, "quantity": 2}
    assert isinstance(Product.new_product(data), Product)


def test_price_getter_returns_value():
    """Геттер возвращает текущую цену."""
    product = Product("Тест", "оп", 2000.0, 5)
    assert product.price == 2000.0


def test_price_setter_valid_updates_price():
    """Сеттер меняет цену, если она положительная."""
    product = Product("Тест", "оп", 2000.0, 5)
    product.price = 3000.0
    assert product.price == 3000.0


def test_price_setter_rejects_zero(capsys):
    """Цена 0 не устанавливается, выводится сообщение."""
    product = Product("Тест", "оп", 2000.0, 5)
    product.price = 0

    assert product.price == 2000.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_price_setter_rejects_negative(capsys):
    """Отрицательная цена не устанавливается, выводится сообщение."""
    product = Product("Тест", "оп", 2000.0, 5)
    product.price = -100

    assert product.price == 2000.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_product_str():
    product = Product("Товар A", "Описание", 100, 10)
    assert str(product) == "Товар A, 100 руб. Остаток: 10 шт."


def test_product_add():
    a = Product("Товар A", "Описание", 100, 10)
    b = Product("Товар B", "Описание", 200, 2)
    assert a + b == 1400


def test_product_add_zero_quantity():
    a = Product("Товар A", "Описание", 100, 0)
    b = Product("Товар B", "Описание", 200, 2)
    assert a + b == 400


def test_product_add_not_supported_type():
    a = Product("Товар A", "Описание", 100, 10)
    with pytest.raises(TypeError):
        a.__add__("строка")


def test_price_getter():
    product = Product("Товар A", "Описание", 100, 10)
    assert product.price == 100


def test_price_setter_valid():
    product = Product("Товар A", "Описание", 100, 10)
    product.price = 150
    assert product.price == 150


def test_new_product_from_dict():
    data = {
        "name": "Товар A",
        "description": "Описание",
        "price": 100,
        "quantity": 10,
    }
    product = Product.new_product(data)
    assert product.name == "Товар A"
    assert product.description == "Описание"
    assert product.price == 100
    assert product.quantity == 10
    assert isinstance(product, Product)


def test_add_same_product_class_ok():
    a = Product("Товар A", "Описание", 100, 10)
    b = Product("Товар B", "Описание", 200, 2)
    assert a + b == 1400


def test_add_same_smartphone_class_ok():
    s1 = Smartphone("Samsung", "оп", 180000.0, 5, "высокая", "S23", 256, "серый")
    s2 = Smartphone("Iphone", "оп", 210000.0, 8, "высокая", "15", 512, "серый")
    assert s1 + s2 == 2580000.0


def test_add_same_lawn_grass_class_ok():
    g1 = LawnGrass("Микс 1", "оп", 350, 50, "Россия", 7, "зелёный")
    g2 = LawnGrass("Микс 2", "оп", 420, 30, "Беларусь", 5, "изумрудный")
    assert g1 + g2 == 30100.0


# ---------- Тесты к заданию: базовый абстрактный класс BaseProduct ----------


def test_base_product_cannot_instantiate():
    """BaseProduct — абстрактный класс, экземпляр создать нельзя."""
    with pytest.raises(TypeError):
        BaseProduct("Товар", "Описание", 100, 10)


def test_base_product_is_abstract():
    """BaseProduct наследуется от ABC и содержит абстрактные методы."""
    assert issubclass(BaseProduct, ABC)


def test_product_is_subclass_of_base_product():
    """Product наследует BaseProduct."""
    assert issubclass(Product, BaseProduct)


def test_smartphone_is_subclass_of_product():
    """Smartphone остаётся наследником Product."""
    s = Smartphone("Samsung", "оп", 180000.0, 5, "высокая", "S23", 256, "серый")
    assert isinstance(s, Smartphone)
    assert isinstance(s, Product)
    assert isinstance(s, BaseProduct)


def test_lawn_grass_is_subclass_of_product():
    """LawnGrass остаётся наследником Product."""
    g = LawnGrass("Микс 1", "оп", 350, 50, "Россия", 7, "зелёный")
    assert isinstance(g, LawnGrass)
    assert isinstance(g, Product)
    assert isinstance(g, BaseProduct)


def test_base_product_abstract_methods():
    """BaseProduct должен объявлять price, __str__, __add__ как абстрактные."""
    assert BaseProduct.__abstractmethods__
    # Проверяем, что нужные методы помечены как абстрактные
    assert "price" in BaseProduct.__abstractmethods__
    assert "__str__" in BaseProduct.__abstractmethods__
    assert "__add__" in BaseProduct.__abstractmethods__


def test_log_mixin_prints_on_product_creation(capsys):
    """При создании Product выводится сообщение в консоль."""
    Product("Продукт1", "Описание продукта", 1200, 10)
    captured = capsys.readouterr()
    assert "Продукт1" in captured.out


def test_log_mixin_prints_class_name(capsys):
    """В сообщении отражается фактический класс объекта."""
    Smartphone("Samsung", "оп", 180000.0, 5, "высокая", "S23", 256, "серый")
    captured = capsys.readouterr()
    assert "Smartphone" in captured.out


def test_log_mixin_in_mro():
    """LogMixin присутствует в цепочке наследования Product."""
    assert LogMixin in Product.__mro__
