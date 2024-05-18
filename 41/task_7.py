from typing import Tuple, Union


class Vector:
    def __init__(self, *args: Union[int, float]) -> None:
        self._array = args

    def __sub__(self, obj: "Vector") -> "Vector":
        self.validate_len(obj)
        return self.__class__(
            *[x - y for x, y in zip(self._array, obj._array)]
        )

    def __add__(self, obj: "Vector") -> "Vector":
        self.validate_len(obj)
        if any(isinstance(i, float) for i in obj.get_coords()):
            return Vector(*[x + y for x, y in zip(self._array, obj._array)])
        return VectorInt(*[x + y for x, y in zip(self._array, obj._array)])

    def validate_len(self, obj: "Vector") -> bool:
        if not len(self._array) == len(obj._array):
            raise TypeError
        return True

    def get_coords(self) -> Tuple[Union[int, float], ...]:
        return self._array


class VectorInt(Vector):
    def __init__(self, *args: int) -> None:
        self.validate_int(args)
        self._array = args

    @staticmethod
    def validate_int(args: Tuple[int, ...]) -> bool:
        if not all(isinstance(i, int) for i in args):
            raise ValueError
        return True


if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(3, 4, 5)

    assert (
        (v1 + v2).get_coords() == (4, 6, 8)
    ), "операция сложения дала неверные значения (или некорректно работает метод get_coords)"
    assert (
        (v1 - v2).get_coords() == (-2, -2, -2)
    ), "операция вычитания дала неверные значения (или некорректно работает метод get_coords)"

    v = VectorInt(1, 2, 3, 4)
    assert isinstance(
        v, Vector
    ), "класс VectorInt должен наследоваться от класса Vector"

    try:
        v = VectorInt(1, 2, 3.4, 4)
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError для команды v = VectorInt(1, 2, 3.4, 4)"

    v1 = VectorInt(1, 2, 3, 4)
    v2 = VectorInt(4, 2, 3, 4)
    v3 = Vector(1.0, 2, 3, 4)

    v = v1 + v2
    assert (
        type(v) == VectorInt
    ), "при сложении вектором с целочисленными координатами должен формироваться объект класса VectorInt"
    v = v1 + v3
    assert (
        type(v) == Vector
    ), "при сложении вектором с вещественными координатами должен формироваться объект класса Vector"
