from typing import Union

Digit = Union[int, float]


class Food:
    def __init__(self, name: str, weight: Digit, calories: int) -> None:
        self._name = name
        self._weight = weight
        self._calories = calories


class BreadFood(Food):
    def __init__(
        self, name: str, weight: Digit, calories: int, white: bool
    ) -> None:
        super().__init__(name, weight, calories)
        self._white = white


class SoupFood(Food):
    def __init__(
        self, name: str, weight: Digit, calories: int, dietary: bool
    ) -> None:
        super().__init__(name, weight, calories)
        self._dietary = dietary


class FishFood(Food):
    def __init__(
        self, name: str, weight: Digit, calories: int, fish: str
    ) -> None:
        super().__init__(name, weight, calories)
        self._fish = fish


if __name__ == "__main__":
    assert issubclass(Food, object)
    f = Food("bread", 50, 250)
    assert hasattr(f, "_name")
    assert hasattr(f, "_weight")
    assert hasattr(f, "_calories")
    assert f._name == "bread"
    assert f._weight == 50
    assert f._calories == 250

    assert issubclass(BreadFood, Food)
    bread = BreadFood("bread", 10, 20, True)
    assert bread._white is True

    assert issubclass(SoupFood, Food)
    soup = SoupFood("sup", 11, 22, False)
    assert soup._dietary is False

    assert issubclass(FishFood, Food)
    fish = FishFood("riba", 1, 2, "s plavnikom")
    assert fish._fish == "s plavnikom"
