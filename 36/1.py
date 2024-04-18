from typing import Union

Digits = Union[int, float]


class Rect:

    def __init__(
        self, x: Digits, y: Digits, width: Digits, height: Digits
    ) -> None:
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def __eq__(self, value) -> bool:
        if isinstance(value, Rect):
            return (
                self._height == value._height and self._width == value._width
            )
        return False

    def __hash__(self):
        return hash((self._width, self._height))


if __name__ == "__main__":
    r1 = Rect(10, 5, 100, 50)
    r2 = Rect(-10, 4, 100, 50)
    assert r1 == r2
    assert hash(r1) == hash(r2)
