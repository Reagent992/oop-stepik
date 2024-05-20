from typing import Any


class Tuple(tuple):
    def __init__(self, array: Any) -> None:
        self.array = tuple(array)

    def __add__(self, obj) -> "Tuple":
        return Tuple((*self.array, *obj))


if __name__ == "__main__":
    t = Tuple([1, 2, 3])
    t = t + "Python"
    print(t)  # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
    t = (t + "Python") + "ООП"
    d = {1, 2, 3}
    t = (t + d)
    print(t)