from typing import Tuple


class ListInteger(list):
    def __init__(self, array: Tuple[int, ...]) -> None:
        self.validate_value(*array)
        super().__init__(array)
        # self.array = list(array)

    def __setitem__(self, index: int, value: int) -> None:
        self.validate_value(value)
        super().__setitem__(index, value)
        # self.array[index] = value

    def append(self, value: int) -> None:
        self.validate_value(value)
        super().append(value)
        # self.array.append(value)

    @staticmethod
    def validate_value(*arg) -> bool:
        if not all(isinstance(i, int) for i in arg):
            raise TypeError
        return True


if __name__ == "__main__":
    a = ListInteger((1, 2, 3))
    assert a == [1, 2, 3]
    try:
        ListInteger((11, 0.5))
    except TypeError:
        assert True
    else:
        assert False
    a.append(4)
    assert a == [1, 2, 3, 4]
    a[0] = 5
    assert a[0] == 5
    assert a == [5, 2, 3, 4]
