import uuid
from typing import Callable, Optional, Type, Union


class Descriptor:
    def __init__(
        self, validator: Optional[Callable] = None, exception=ValueError
    ) -> None:
        self.validator = validator
        self.exception = exception

    def __set_name__(self, owner: Type[object], name: str):
        self.private_name = f"_{owner.__name__}__{name}"

    def __get__(self, obj: object, objtype=None):
        return getattr(obj, self.private_name, None)

    def __set__(self, obj: object, value) -> None:
        if self.validator is not None:
            if self.validator(value):
                setattr(obj, self.private_name, value)
            else:
                raise ValueError(f"{value} must be positive")


def validate_positive_digit(value: Union[int, float]) -> bool:
    return value > 0


class ShopInterface:
    def get_id(self):
        raise NotImplementedError("в классе не переопределен метод get_id")


class ShopItem(ShopInterface):
    _weight = Descriptor(validate_positive_digit)
    _price = Descriptor(validate_positive_digit)

    def __init__(
        self, name: str, weight: Union[int, float], price: Union[int, float]
    ) -> None:
        self.__id = uuid.uuid4().int
        self._name = name
        self._weight = weight
        self._price = price

    def get_id(self) -> int:
        return self.__id


if __name__ == "__main__":
    assert issubclass(ShopInterface, object)
    assert hasattr(ShopInterface, "get_id")
    try:
        ShopInterface().get_id()
    except NotImplementedError as e:
        assert str(e) == "в классе не переопределен метод get_id"
    else:
        assert False

    assert issubclass(ShopItem, ShopInterface)
    item = ShopItem("name", 10, 1000)
    assert item._name == "name"
    assert item._weight == 10
    assert item._price == 1000
    assert hasattr(item, "_ShopItem__id")
    assert isinstance(item._ShopItem__id, int)
    try:
        ShopItem("name", -1, -1)
    except ValueError:
        assert True
    else:
        assert False
    assert hasattr(item, "get_id")
    assert item.get_id() == item._ShopItem__id
