from typing import Any, Union


class Circle:
    def __init__(
        self,
        x: Union[int, float],
        y: Union[int, float],
        radius: Union[int, float],
    ) -> None:
        self.x = x
        self.y = y
        self.radius = radius

    @property
    def x(self) -> Union[int, float]:
        return self.__x

    @x.setter
    def x(self, value) -> None:
        if isinstance(value, (int, float)):
            self.__x = value
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    @property
    def y(self) -> Union[int, float]:
        return self.__y

    @y.setter
    def y(self, value) -> None:
        if isinstance(value, (int, float)):
            self.__y = value
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    @property
    def radius(self) -> Union[int, float]:
        return self.__radius

    @radius.setter
    def radius(self, value) -> None:
        if isinstance(value, (int, float)):
            if 0 < value:
                self.__radius = value
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __getattr__(self, item: Any) -> bool:
        return False


# circle = Circle(10.5, 7, 22)
# circle.radius = (
#     -10
# )  # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
# assert circle.radius == 22
# x, y = circle.x, circle.y
# assert x == 10.5
# assert y == 7
# assert circle.name is False  # False, т.к. атрибут name не существует
# try:
#     c1 = Circle("ф", 0, 0)  # type: ignore
# except TypeError:
#     print("TypeError работает")


assert (
    type(Circle.x) == property
    and type(Circle.y) == property
    and type(Circle.radius) == property
), "в классе Circle должны быть объявлены объекты-свойства x, y и radius"

try:
    cr = Circle(20, "7", 22)
except TypeError:
    assert True
else:
    assert (
        False
    ), "не сгенерировалось исключение TypeError при инициализации объекта с недопустимыми аргументами"

cr = Circle(20, 7, 22)
assert (
    cr.x == 20 and cr.y == 7 and cr.radius == 22
), "объекты-свойства x, y и radius вернули неверные значения"

cr.radius = (
    -10
)  # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
assert (
    cr.radius == 22
), "при присваивании некорректного значения, прежнее значение изменилось"

x, y = cr.x, cr.y
assert (
    x == 20 and y == 7
), "объекты-свойства x, y вернули некорректные значения"
assert (
    cr.name == False
), "при обращении к несуществующему атрибуту должно возвращаться значение False"

try:
    cr.x = "20"
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"

cr.y = 7.8
cr.radius = 10.6
