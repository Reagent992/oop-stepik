from typing import List


class StringValue:
    def __init__(self, min_length: int = 2, max_length: int = 50) -> None:
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if self.validate(value):
            setattr(obj, self.private_name, value)

    def validate(self, value: str) -> bool:
        return (
            isinstance(value, str)
            and self.min_length <= len(value) <= self.max_length
        )


class PriceValue:
    def __init__(self, max_value: int = 10000) -> None:
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if self.validate(value):
            setattr(obj, self.private_name, value)

    def validate(self, value: int) -> bool:
        return isinstance(value, int) and 0 <= value <= self.max_value


class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self, name: str = "", price: int = 0) -> None:
        self.name = name
        self.price = price


class SuperShop:
    def __init__(self, name: str) -> None:
        self.name = name
        self.goods: List[Product] = list()

    def add_product(self, product: Product) -> None:
        """Добавление товара в магазин."""
        self.goods.append(product)

    def remove_product(self, product: Product) -> None:
        """Удаление товара из магазина."""
        self.goods.remove(product)


if __name__ == "__main__":
    # add\delete
    m = SuperShop("Магаз под-пиваса")
    pivo = Product("Пивас", 99)
    m.add_product(pivo)
    assert m.goods == [pivo]
    m.remove_product(pivo)
    assert m.goods == []

    # values
    t = Product("Ы", -3)
    try:
        assert t.name != "Ы" and t.price == 0
    except AttributeError:
        True
