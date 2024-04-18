from typing import Union


class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(
        self, x: Union[int, float] = 0, y: Union[int, float] = 0
    ) -> None:
        if x and self.type_check(x):
            self.__x = x
        else:
            self.__x = 0
        if y and self.type_check(y):
            self.__y = y
        else:
            self.__y = 0

    @classmethod
    def type_check(cls, value: Union[int, float]) -> bool:
        return (
            isinstance(value, (int, float))
            and cls.MIN_COORD <= value <= cls.MAX_COORD
        )

    @property
    def x(self) -> Union[int, float]:
        return self.__x

    @x.setter
    def x(self, value: Union[int, float]) -> None:
        if self.type_check(value):
            self.__x = value

    @property
    def y(self) -> Union[int, float]:
        return self.__y

    @y.setter
    def y(self, value: Union[int, float]) -> None:
        if self.type_check(value):
            self.__y = value

    def norm2(vector: "RadiusVector2D") -> Union[int, float]:
        return vector.__x * vector.__x + vector.__y * vector.__y


v1 = RadiusVector2D()  # радиус-вектор с координатами (0; 0)
v2 = RadiusVector2D(1)  # радиус-вектор с координатами (1; 0)
v3 = RadiusVector2D(1, 2)  # радиус-вектор с координатами (1; 2)
v4 = RadiusVector2D("a")
v5 = RadiusVector2D(10000)
assert v5.x == 0
assert v4.x == 0
v2.y = 3
assert v2.y == 3
assert v2.x == 1
assert v1.x == 0
