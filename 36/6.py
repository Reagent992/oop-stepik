from math import sqrt
from typing import Union


class Descriptor:
    def __set_name__(self, owner, name: str):
        self.private_name = f"_{name}"

    def __get__(self, obj: object, objtype=None):
        return getattr(obj, self.private_name, None)

    def __set__(self, obj: object, value) -> None:
        if isinstance(value, (int, float)) and value > 0:
            setattr(obj, self.private_name, value)
        else:
            raise ValueError(
                "длины сторон треугольника должны быть положительными числами"
            )


class Triangle:
    a = Descriptor()
    b = Descriptor()
    c = Descriptor()

    def __init__(
        self,
        a: Union[int, float],
        b: Union[int, float],
        c: Union[int, float],
    ) -> None:
        self.a = a
        self.b = b
        self.c = c

    # @property
    # def a(self) -> Optional[Union[int, float]]:
    #     if self.a:
    #         return self.a
    #     return None

    # @a.setter
    # def a(self, value) -> None:
    #     if self.validate(value):
    #         if self.b and self.c:
    #             if self.validate_triangle(value, self.b, self.c):
    #                 self.a = value
    #         else:
    #             self.a = value

    # @property
    # def b(self) -> Optional[Union[int, float]]:
    #     if self.b:
    #         return self.b
    #     return None

    # @b.setter
    # def b(self, value) -> None:
    #     if self.validate(value):
    #         if self.a and self.c:
    #             if self.validate_triangle(value, self.a, self.c):
    #                 self.b = value
    #         else:
    #             self.b = value

    # @property
    # def c(self) -> Optional[Union[int, float]]:
    #     if self.c:
    #         return self.c
    #     return None

    # @c.setter
    # def c(self, value) -> None:
    #     if self.validate(value):
    #         if self.a and self.b:
    #             if self.validate_triangle(value, self.a, self.b):
    #                 self.c = value
    #         else:
    #             self.c = value

    def __setattr__(self, key: str, value: Union[int, float]) -> None:
        # if isinstance(value, (int, float)) and value > 0:
        #     super().__setattr__(name, value)
        # else:
        #     raise ValueError(
        #         "длины сторон треугольника должны быть положительными числами"
        #     )
        if (
            (key == "a" and not self.validate_triangle(value, self.b, self.c))
            or (
                key == "b"
                and not self.validate_triangle(self.a, value, self.c)
            )
            or (
                key == "c"
                and not self.validate_triangle(self.a, self.b, value)
            )
        ):
            raise ValueError(
                "с указанными длинами нельзя образовать треугольник"
            )
        super().__setattr__(key, value)

    # @staticmethod
    # def validate(value) -> bool:
    #     if isinstance(value, (int, float)) and value > 0:
    #         return True
    #     else:
    #         raise ValueError(
    #             "длины сторон треугольника должны быть положительными числами"
    #         )

    @staticmethod
    def validate_triangle(
        a: Union[int, float], b: Union[int, float], c: Union[int, float]
    ) -> bool:
        if a and b and c:
            return a < b + c and b < a + c and c < a + b
        return True
        # if a < b + c and b < a + c and c < a + b:
        #     return True
        # else:
        #     raise ValueError(
        #         "с указанными длинами нельзя образовать треугольник"
        #     )

    def __len__(self) -> int:
        """Периметр треугольника."""
        return int(self.a + self.b + self.c)

    def __call__(self) -> float:
        """Площадь треугольника."""
        p = (self.a + self.b + self.c) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


if __name__ == "__main__":
    tr = Triangle(2, 2, 2)
    try:
        tr.a = -1
    except ValueError:
        pass
    try:
        tr.b = -1
    except ValueError:
        pass
    try:
        tr.c = -1
    except ValueError:
        pass
    try:
        tr.c = 0
    except ValueError:
        pass
    # selfedu
        tr = Triangle(5, 4, 3)
    assert (
        tr.a == 5 and tr.b == 4 and tr.c == 3
    ), "дескрипторы вернули неверные значения"

    try:
        tr = Triangle(-5, 4, 3)
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError"

    try:
        tr = Triangle(10, 1, 1)
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError"

    tr = Triangle(5, 4, 3)
    assert len(tr) == 12, "функция len вернула неверное значение"
    assert 5.9 < tr() < 6.1, "метод __call__ вернул неверное значение"
