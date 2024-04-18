class Line:
    def __init__(
        self, x1: int = 0, y1: int = 0, x2: int = 0, y2: int = 0
    ) -> None:
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

    def set_coords(self, x1: int, y1: int, x2: int, y2: int):
        """для изменения координат линии."""
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

    def get_coords(self) -> tuple:
        """для получения кортежа из текущих координат линии."""
        return (self.__x1, self.__y1, self.__x2, self.__y2)

    def draw(self) -> None:
        """для отображения в консоли списка
        текущих координат линии (в одну строчку через пробел)"""
        print(*self.get_coords())


l = Line(1, 2, 3, 4)
l.set_coords(5, 6, 7, 8)
l_r = l.get_coords()
assert l_r == (5, 6, 7, 8)
l.draw()
