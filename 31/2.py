from typing import Any, List, Union


class Shop:
    def __init__(self, name: str) -> None:
        self.name = name
        self.goods: List[Product] = list()

    def add_product(self, product: "Product"):
        self.goods.append(product)

    def remove_product(self, product: "Product"):
        self.goods.remove(product)


class Product:
    last_id = 0

    def __init__(
        self, name: str, weight: Union[int, float], price: Union[int, float]
    ) -> None:
        self.id = self.__id_generator()
        self.name = name
        self.weight = weight
        self.price = price

    @classmethod
    def __id_generator(cls):
        cls.last_id += 1
        return cls.last_id

    def __setattr__(self, attr: str, value: Any) -> None:
        if attr in ("name",) and isinstance(value, str):
            super().__setattr__(attr, value)
        elif attr in ("id", "weight", "price") and isinstance(
            value, (int, float)
        ):
            if 0 < value:
                super().__setattr__(attr, value)
            else:
                raise TypeError()
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, name: str) -> None:
        if name == "id":
            raise AttributeError("Атрибут id удалять запрещено.")
        super().__delattr__(name)


if __name__ == "__main__":
    p = Product("a", 1, 1)
    p2 = Product("a", 1, 1)
    try:
        del p.id
    except AttributeError:
        True
    try:
        p.weight == 0
    except TypeError:
        True
