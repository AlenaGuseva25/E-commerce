from typing import List

from src.abstract_classes import BaseProduct
from src.mixin import LogMixin


class Product(LogMixin, BaseProduct):
    """Класс для представления продукта"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity <= 0:
            raise ValueError("Товар с нулевым или отрицательным количеством не может быть добавлен.")
        super().__init__(name, description, price, quantity)

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Общая стоимость"""
        if isinstance(other, BaseProduct):
            total_value = (self.price * self.quantity) + (other.price * other.quantity)
            return total_value
        return NotImplemented

    @classmethod
    def new_product(cls, product_dict: dict):
        """Создает новый объект класса Product из словаря с параметрами товара"""
        return cls(
            name=product_dict["name"],
            description=product_dict["description"],
            price=product_dict["price"],
            quantity=product_dict["quantity"],
        )


class Category:
    """Класс для представления категории продуктов"""

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product] = None):
        self.name: str = name
        self.description: str = description
        self.__products: List[Product] = products if products else []

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product):
        """Добавление продукта в категорию и обновление количества товаров"""
        if not isinstance(product, Product):
            raise TypeError(
                f"Нельзя добавить объект {type(product).__name__}. Ожидался экземпляр Product или его наследника."
            )

        self.__products.append(product)
        Category.product_count += 1
        print(f"Продукт '{product.name}' добавлен в категорию '{self.name}'.")

    @property
    def products(self):
        """Геттер для получения списка продуктов в категории в виде строк"""
        return "\n".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__products
        )

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity}"

    def middle_price(self):
        """Средний ценник товаров в категории"""
        try:
            middle_price = sum(product.price for product in self.__products)
            return middle_price / len(self.__products)
        except ZeroDivisionError:
            return 0
