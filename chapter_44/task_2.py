from typing import Any, Tuple, Union

Digit = Union[int, float]


class Furniture:
    def __init__(self, name: str, weight: Digit) -> None:
        self._name = name
        self._weight = weight

    def __verify_name(self, name: str) -> bool:
        if not isinstance(name, str):
            raise TypeError
        return True

    def __verify_weight(self, weight: Digit) -> bool:
        if not isinstance(weight, (int, float)):
            raise TypeError
        return True

    def _verify_positive_digit(self, value: Digit) -> bool:
        if not value > 0:
            raise ValueError
        return True

    def __setattr__(self, name: str, value: Any) -> None:
        if name == "_name":
            self.__verify_name(value)
        elif name == "_weight":
            self.__verify_weight(value)
        super().__setattr__(name, value)

    def get_attrs(self) -> Tuple[Any, ...]:
        return tuple(self.__dict__.values())


class Closet(Furniture):
    def __init__(self, name: str, weight: Digit, tp: bool, doors: int) -> None:
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors


class Chair(Furniture):
    def __init__(self, name: str, weight: Digit, height: Digit) -> None:
        super().__init__(name, weight)
        self._height = height

    def __setattr__(self, name: str, value: Any) -> None:
        if name == "_height":
            self._verify_positive_digit(value)
        super().__setattr__(name, value)


class Table(Furniture):
    def __init__(
        self, name: str, weight: Digit, height: Digit, square: Digit
    ) -> None:
        super().__init__(name, weight)
        self._height = height
        self._square = square

    def __setattr__(self, name: str, value: Any) -> None:
        if name == "_height":
            self._verify_positive_digit(value)
        super().__setattr__(name, value)


if __name__ == "__main__":
    cl = Closet("шкаф-купе", 342.56, True, 3)
    chair = Chair("стул", 14, 55.6)
    tb = Table("стол", 34.5, 75, 10)
    print(tb.get_attrs())
    try:
        Furniture(10, 10)  # type: ignore
    except TypeError:
        assert True
    else:
        assert False
