from typing import List

class Product:
    """Класс для представления продукта"""
    def __init__(self, name, description, price, quantity):
        self.name: str = name
        self.description: str = description
        self.price: float = price
        self.quantity: int = quantity


class Category:
    """Класс для представления категории продуктов"""
    total_categories: int = 0
    total_products: int = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        self.name: str = name
        self.description: str = description
        self.products: List[Product] = products if products else []

        Category.total_categories += 1
        Category.total_products += len(self.products)

    def add_product(self, product: Product):
        """Добавление продукт в категорию и обновляет количество товаров"""
        self.products.append(product)
        Category.total_products += 1





