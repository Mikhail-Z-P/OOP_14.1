from abc import ABC, abstractmethod

class BaseProduct(ABC):
    """Базовый абстрактный класс для всех продуктов."""

    @property
    @abstractmethod
    def price(self):
        """Цена с валидацией."""

    @abstractmethod
    def __str__(self):
        """Строковое представление."""

    @abstractmethod
    def __add__(self, other):
        """Сложение товаров одного класса."""

class LogMixin:
    """Миксин: логирует создание объекта с параметрами."""
    def __init__(self, *args, **kwargs):
        args_repr = ", ".join(repr(a) for a in args)
        print(f"{self.__class__.__name__}({args_repr})")
        super().__init__(**kwargs)

class Product(BaseProduct, LogMixin):
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError(
                f"Нельзя складывать товары разных классов: "
                f"{type(self).__name__} и {type(other).__name__}"
            )
        full_cost = self.price * self.quantity
        other_full_cost = other.price * other.quantity
        return full_cost + other_full_cost


class Smartphone(Product):
    """Смартфон"""

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Трава газонная"""

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

