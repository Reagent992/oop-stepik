from math import sqrt
from typing import List, Tuple


class RadiusVector:
    """n-мерный массив."""

    def __init__(self, *args) -> None:
        self.validate(*args)
        if len(args) == 1:
            self.__vector: List[int] = [0] * args[0]
        else:
            self.__vector = list(args)

    def __len__(self) -> int:
        return len(self.__vector)

    def __abs__(self) -> float:
        """Возвращает длину радиус-вектора."""
        return sqrt(sum([i * i for i in self.__vector]))

    def set_coords(self, *args) -> None:
        """Изменения координат радиус-вектора."""
        self.validate(*args)
        n = min(len(args), len(self.__vector))
        self.__vector[:n] = args[:n]

    def get_coords(self) -> Tuple[int, ...]:
        """получения текущих координат радиус-вектора (в виде кортежа)."""
        return tuple(self.__vector)

    @staticmethod
    def validate(*args):
        if all(isinstance(x, int) for x in args):
            return True
        else:
            raise TypeError


if __name__ == "__main__":
    v = RadiusVector(5)
    v.set_coords(1, 2, 3, 4, 5)
    assert v.get_coords() == (1, 2, 3, 4, 5)
    assert len(v) == 5
    assert abs(v) == 7.416198487095663

    v.set_coords(6, 7)
    assert v.get_coords() == (6, 7, 3, 4, 5)
    v.set_coords(0)
    assert v.get_coords() == (0, 7, 3, 4, 5)
