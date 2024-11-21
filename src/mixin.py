class LogMixin:
    """Печатает в консоль информацию о том, от какого класса и с какими параметрами был создан объект"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(
            f"Создан объект {self.__class__.__name__} с параметрами: {args}, {kwargs}"
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(name={self.name}, description={self.description}, price={self.price},"
            f" quantity={self.quantity})"
        )
