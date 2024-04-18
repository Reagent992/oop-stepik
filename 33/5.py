from typing import Union


class Complex:
    """Работа с комплексными числами."""

    def __init__(
        self,
        real: Union[int, float],  # Действительная часть.
        img: Union[int, float],  # Мнимая часть.
    ) -> None:
        self.__real = real
        self.__img = img

    @property
    def real(self) -> Union[int, float]:
        return self.__real

    @real.setter
    def real(self, value: Union[int, float]) -> None:
        if self.validate(value):
            self.__real = value

    @property
    def img(self) -> Union[int, float]:
        return self.__img

    @img.setter
    def img(self, value: Union[int, float]) -> None:
        if self.validate(value):
            self.__img = value

    def __abs__(self) -> float:
        return (self.real * self.real + self.img * self.img) ** 0.5

    def validate(self, value: Union[int, float]) -> bool:
        if type(value) in (int, float):
            return True
        raise ValueError("Неверный тип данных.")


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
