from typing import Union


class Descriptor:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __set_name__(self, owner: object, name: str):
        self.private_name = f"_{owner.__name__}__{name}"

    def __get__(self, obj: object, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj: object, value) -> None:
        if self.validate(value):
            setattr(obj, self.private_name, value)

    def validate(self, value) -> bool:
        return self.MIN_DIMENSION <= value <= self.MAX_DIMENSION


class Dimensions:
    """Габариты."""

    a, b, c = Descriptor(), Descriptor(), Descriptor()

    def __init__(self, a: int, b: int, c: int) -> None:
        self.a = a
        self.b = b
        self.c = c

    def get_volume(self) -> int:
        return self.a * self.b * self.c

    def __gt__(self, obj: "Dimensions") -> bool:
        return self.get_volume() > obj.get_volume()

    def __lt__(self, obj: "Dimensions") -> bool:
        return self.get_volume() < obj.get_volume()

    def __ge__(self, obj: "Dimensions") -> bool:
        return self.get_volume() >= obj.get_volume()

    def __le__(self, obj: "Dimensions") -> bool:
        return self.get_volume() <= obj.get_volume()


class ShopItem:
    """Товар."""

    def __init__(
        self, name: str, price: Union[int, float], dim: Dimensions
    ) -> None:
        self.name = name
        self.price = price
        self.dim = dim


trainers = ShopItem("кеды", 1024, Dimensions(40, 30, 120))
umbrella = ShopItem("зонт", 500.24, Dimensions(10, 20, 50))
fridge = ShopItem("холодильник", 40000, Dimensions(2000, 600, 500))
chair = ShopItem("табуретка", 2000.99, Dimensions(500, 200, 200))
lst_shop = [trainers, umbrella, fridge, chair]
lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim.get_volume())

if __name__ == "__main__":
    # Проверка Dimensions
    d1 = Dimensions(10, 20, 30)
    assert d1.a == 10 and d1.b == 20 and d1.c == 30
    assert d1.get_volume() == 6000
    # Сравнение.
    d2 = Dimensions(20, 20, 30)
    assert (d1 < d2) is True

    # Проверка ShopItem
    si1 = ShopItem("Мопед", 3000, d1)
    assert si1.name == "Мопед" and si1.price == 3000 and si1.dim == d1
    assert [i.name for i in lst_shop_sorted] == [
        "зонт",
        "кеды",
        "табуретка",
        "холодильник",
    ]
