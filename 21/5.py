from typing import Union


def check_number_cords(*cords):
    """Проверка типов цифр."""
    return all([isinstance(i, (int, float)) for i in cords])


class Point:
    def __init__(self, x: Union[int, float], y: Union[int, float]) -> None:
        if check_number_cords(x, y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Передан неверный тип аргументов.")

    def get_coords(self):
        """Получение кортежа из значений точки."""
        return self.__x, self.__y


class Rectangle:
    def __init__(self, *cords: Union[int, float, Point]) -> None:
        if len(cords) == 2 and self.check_point_cords(*cords):
            self.__sp = cords[0]
            self.__ep = cords[1]
        elif len(cords) == 4 and check_number_cords(*cords):
            self.__ep = Point(cords[0], cords[1])
            self.__sp = Point(cords[2], cords[3])
        else:
            raise ValueError("Переданно неверное количество аргументов")

    def set_coords(self, sp, ep) -> None:
        """изменение текущих координат, где sp, ep - объекты класса Point;"""
        if self.check_point_cords(sp, ep):
            self.__ep = ep
            self.__sp = sp
        else:
            raise ValueError("Передан неверный тип аргументов.")

    def get_coords(self) -> tuple:
        """возвращение кортежа из объектов класса Point
        с текущими координатами"""
        return self.__sp, self.__ep

    def draw(self):
        """отображение в консоли сообщения"""
        print(
            f"Прямоугольник с координатами: {self.__ep.get_coords()} "
            f"{self.__sp.get_coords()}"
        )

    @classmethod
    def check_point_cords(cls, *points):
        """Проверка типов точек."""
        return all([isinstance(i, Point) for i in points])


rect = Rectangle(Point(0, 0), Point(20, 34))

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = Point(5, 6)
p4 = Point(7, 8)
r1 = Rectangle(p1, p2)
assert r1.get_coords() == (p1, p2)
r1.set_coords(p3, p4)
assert r1.get_coords() == (p3, p4)

r2 = Rectangle(1, 2, 3, 4)
r2.draw()
