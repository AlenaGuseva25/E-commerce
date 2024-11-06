from src.classes import Product, Category


def test_product_initialization():
    product = Product("Товар 1", "Описание товара 1", 100.0, 10)
    assert product.name == "Товар 1"
    assert product.description == "Описание товара 1"
    assert product.price == 100.0
    assert product.quantity == 10


def test_category_initialization():
    category = Category("Категория 1", "Описание категории 1")
    assert category.name == "Категория 1"
    assert category.description == "Описание категории 1"
    assert category.products == []
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_category_with_products_initialization():
    product1 = Product("Товар 1", "Описание товара 1", 100.0, 10)
    product2 = Product("Товар 2", "Описание товара 2", 200.0, 5)
    category = Category("Категория 1", "Описание категории 1", products=[product1, product2])

    assert category.name == "Категория 1"
    assert category.description == "Описание категории 1"
    assert len(category.products) == 2
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_add_product():
    category = Category("Категория 1", "Описание категории 1")
    product = Product("Товар 1", "Описание товара 1", 100.0, 10)

    category.add_product(product)

    assert len(category.products) == 1
    assert category.products[0].name == "Товар 1"
    assert Category.product_count == 1


def test_add_multiple_products():
    category = Category("Категория 1", "Описание категории 1")
    product1 = Product("Товар 1", "Описание товара 1", 100.0, 10)
    product2 = Product("Товар 2", "Описание товара 2", 200.0, 5)

    category.add_product(product1)
    category.add_product(product2)

    assert len(category.products) == 2
    assert Category.product_count == 2
