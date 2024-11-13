from typing import List


class Product:
    """Класс для представления продукта"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name: str = name
        self.description: str = description
        self.__price: float = price
        self.quantity: int = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @property
    def price(self):
        """Геттер для получения цены продукта"""
        return self.__price

    @price.setter
    def price(self, value: float):
        """Сеттер для установки цены продукта с проверкой"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    def __add__(self, other):
        """Общая стоимость"""
        if isinstance(other, Product):
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
        self.__products.append(product)
        Category.product_count += 1

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
