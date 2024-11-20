from abc import ABC, abstractmethod

class BaseProduct(ABC):
    """Абстрактный базовый класс, родитель Product"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        self.__price = value

    @abstractmethod
    def __str__(self):
        """Абстрактный метод для строкового представления продукта"""
        pass

    @abstractmethod
    def __add__(self, other):
        """Абстрактный метод для сложения продуктов"""
        pass


