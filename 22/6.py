from typing import List


class LineTo:
    """Описание маршрутов, состоящих из линейных сегментов."""

    def __init__(self, x: int = 0, y: int = 0) -> None:
        """Координата линейного участка."""
        self.x = x
        self.y = y


class PathLines:
    def __init__(self, *lines: LineTo) -> None:
        self.path: List[LineTo] = list()
        first_point = LineTo()
        lines = (first_point, *lines)
        for line in lines:
            self.add_line(line)

    def add_line(self, line: LineTo) -> None:
        """добавление нового линейного сегмента
        (объекта класса LineTo) в конец маршрута."""
        self.path.append(line)

    def get_path(self) -> List[LineTo]:
        """список из объектов класса LineTo"""
        result: List[LineTo] = []
        for i in self.path:
            result.append(i)
        return result[1:]

    def get_length(self) -> float:
        """возвращает суммарную длину пути
        (сумма длин всех линейных сегментов)"""
        g = (
            (self.path[i - 1], self.path[i]) for i in range(1, len(self.path))
        )
        return sum(
            map(
                lambda t: ((t[0].x - t[1].x) ** 2 + (t[0].y - t[1].y) ** 2)
                ** 0.5,
                g,
            )
        )


if __name__ == "__main__":
    # l1 = LineTo()
    # l2 = LineTo(1, 1)
    # l3 = LineTo(1, 1)
    # assert l1.x == 0 and l1.y == 0
    # assert l2.x == 1 and l2.y == 1
    # assert l3.x == 1 and l3.y == 1
    # p = PathLines()  # начало маршрута из точки 0, 0
    # p = PathLines(
    #     l1,
    #     l2,
    # )  # начало маршрута из точки 0, 0
    # assert p.get_path() == [l1, l2]
    p = PathLines(LineTo(1, 2))
    print(p.get_length())  # 2.23606797749979
    p.add_line(LineTo(10, 20))
    p.add_line(LineTo(5, 17))
    print(p.get_length())  # 28.191631669843197
    m = p.get_path()
    print(all(isinstance(i, LineTo) for i in m) and len(m) == 3)  # True

    h = PathLines(LineTo(4, 8), LineTo(-10, 30), LineTo(14, 2))
    print(h.get_length())  # 71.8992593599813

    k = PathLines()
    print(k.get_length())  # 0
    print(k.get_path())  # []
