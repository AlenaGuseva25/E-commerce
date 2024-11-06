from typing import List

class Product:
    """Класс для представления продукта"""
    name: str
    description: str
    price: float
    quantity: int
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    name: str
    description: str
    products: List[Product]
    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
