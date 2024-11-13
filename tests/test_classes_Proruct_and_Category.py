import pytest
from src.classes import Product, Category


class TestProduct:
    def test_product_initialization(self):
        product = Product(name="Пупа", description="Лупа", price=30.0, quantity=100)
        assert product.name == "Пупа"
        assert product.description == "Лупа"
        assert product.price == 30.0
        assert product.quantity == 100

    def test_price_setter_and_getter(self):
        product = Product(name="Пупа", description="Лупа", price=30.0, quantity=100)
        product.price = 50.0
        assert product.price == 50.0

        product.price = -10
        assert product.price == 50.0

    def test_new_product_class_method(self):
        product_dict = {
            "name": "Груша",
            "description": "Сочные груши",
            "price": 25.0,
            "quantity": 80,
        }
        product = Product.new_product(product_dict)
        assert product.name == "Груша"
        assert product.description == "Сочные груши"
        assert product.price == 25.0
        assert product.quantity == 80


class TestCategory:
    def test_category_initialization(self):
        category = Category(name="Фрукты", description="Свежие фрукты")
        assert category.name == "Фрукты"
        assert category.description == "Свежие фрукты"
        assert category.products == ""

    def test_add_product(self):
        category = Category(name="Фрукты", description="Свежие фрукты")
        product = Product(
            name="Яблоко", description="Свежие красные яблоки", price=30.0, quantity=100
        )
        category.add_product(product)

        assert len(category._Category__products) == 1
        assert category.products == "Яблоко, 30.0 руб. Остаток: 100 шт."

    def test_multiple_products(self):
        category = Category(name="Фрукты", description="Свежие фрукты")
        product1 = Product(
            name="Яблоко", description="Свежие красные яблоки", price=30.0, quantity=100
        )
        product2 = Product(
            name="Груша", description="Сочные груши", price=25.0, quantity=80
        )

        category.add_product(product1)
        category.add_product(product2)

        assert len(category._Category__products) == 2
        expected_output = (
            "Яблоко, 30.0 руб. Остаток: 100 шт.\n" "Груша, 25.0 руб. Остаток: 80 шт."
        )
        assert category.products == expected_output


if __name__ == "__main__":
    pytest.main()
