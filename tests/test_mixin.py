from src.classes import Product


class TestLogMixin:
    def test_log_mixin_initialization(self, capfd):
        product = Product(
            name="Тестовый продукт",
            description="Описание продукта",
            price=10.0,
            quantity=5,
        )

        captured = capfd.readouterr()

        assert "Создан объект Product с параметрами:" in captured.out
        assert "('Тестовый продукт', 'Описание продукта', 10.0, 5)" in captured.out

    def test_repr(self):
        product = Product(
            name="Тестовый продукт",
            description="Описание продукта",
            price=10.0,
            quantity=5,
        )

        assert (
            repr(product) == "Product(name=Тестовый продукт, description=Описание продукта, price=10.0, quantity=5)"
        )
