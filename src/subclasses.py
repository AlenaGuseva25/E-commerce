from src.classes import Product, Category

class Smartphone(Product):
    """Дочерний класс"""
    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency: float,
                 model: str, memory: str, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return (f"{super().__str__()}, Эффективность: {self.efficiency}, Модель: {self.model}, "
                f"Память: {self.memory}, Цвет: {self.color}")

    def __add__(self, other):
        """Сложение продуктов из одинаковых классов"""
        if not isinstance(other, Product):
            return NotImplemented
        if type(self) is not type(other):
            raise TypeError(f"Запрещено складывать продукты разных классов")

        total_value = (self.price * self.quantity) + (other.price * other.quantity)
        return total_value



class LawnGrass(Product):
    """Дочерний класс"""
    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, germination_period: str,
                 color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """Сложение продуктов из одинаковых классов"""
        if not isinstance(other, Product):
            return NotImplemented
        if type(self) is not type(other):
            raise TypeError(f"Запрещено складывать продукты разных классов")

        total_value = (self.price * self.quantity) + (other.price * other.quantity)
        return total_value
