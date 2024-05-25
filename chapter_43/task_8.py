from typing import Any, Union


class ItemAttrs:
    def __getitem__(self, index: int) -> Any:
        return self.__dict__[list(self.__dict__.keys())[index]]

    def __setitem__(self, index: int, value: Any) -> None:
        self.__dict__[list(self.__dict__.keys())[index]] = value


class Point(ItemAttrs):
    def __init__(self, x: Union[int, float], y: Union[int, float]) -> None:
        self.x = x
        self.y = y


if __name__ == "__main__":
    pt = Point(1, 2.5)
    assert pt[0] == 1
    assert pt[1] == 2.5
    pt[0] = 10
    assert pt[0] == 10
