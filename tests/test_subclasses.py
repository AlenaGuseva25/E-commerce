import pytest
from src.subclasses import Smartphone, LawnGrass


def test_smartphone_initialization():
    phone = Smartphone("iPhone 13", "Смартфон от Apple", 999.99, 10, 9.5, "A2634", "128 ГБ", "черный")
    assert phone.name == "iPhone 13"
    assert phone.price == 999.99
    assert phone.quantity == 10
    assert phone.efficiency == 9.5
    assert phone.model == "A2634"
    assert phone.memory == "128 ГБ"
    assert phone.color == "черный"


def test_lawn_grass_initialization():
    grass = LawnGrass("Газонная трава", "Смесь для газона", 25.0, 50, "Россия", "7-14 дней", "зеленый")
    assert grass.name == "Газонная трава"
    assert grass.price == 25.0
    assert grass.quantity == 50
    assert grass.country == "Россия"
    assert grass.germination_period == "7-14 дней"
    assert grass.color == "зеленый"


def test_smartphone_str():
    phone = Smartphone("iPhone 13", "Смартфон от Apple", 999.99, 10, 9.5, "A2634", "128 ГБ", "черный")
    assert str(phone) == ("iPhone 13, 999.99 руб. Остаток: 10 шт., "
                          "Эффективность: 9.5, Модель: A2634, Память: 128 ГБ, Цвет: черный")


def test_lawn_grass_str():
    grass = LawnGrass("Газонная трава", "Смесь для газона", 25.0, 50, "Россия", "7-14 дней", "зеленый")
    assert str(grass) == ("Газонная трава, 25.0 руб. Остаток: 50 шт.")


def test_smartphone_add():
    phone1 = Smartphone("iPhone 13", "Смартфон от Apple", 999.99, 10, 9.5, "A2634", "128 ГБ", "черный")
    phone2 = Smartphone("iPhone 12", "Смартфон от Apple", 799.99, 5, 8.5, "A2403", "64 ГБ", "белый")
    assert phone1 + phone2 == (999.99 * 10) + (799.99 * 5)


def test_lawn_grass_add():
    grass1 = LawnGrass("Газонная трава", "Смесь для газона", 25.0, 50, "Россия", "7-14 дней", "зеленый")
    grass2 = LawnGrass("Газонная трава", "Смесь для газона", 30.0, 30, "США", "10-15 дней", "синий")
    assert grass1 + grass2 == (25.0 * 50) + (30.0 * 30)


def test_add_different_products():
    phone = Smartphone("iPhone 13", "Смартфон от Apple", 999.99, 10, 9.5, "A2634", "128 ГБ", "черный")
    grass = LawnGrass("Газонная трава", "Смесь для газона", 25.0, 50, "Россия", "7-14 дней", "зеленый")

    with pytest.raises(TypeError, match="Запрещено складывать продукты разных классов"):
        phone + grass