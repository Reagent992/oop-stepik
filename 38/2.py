from typing import Union


d = Union[int, float]  # digits


class Track:
    def __init__(self, start_x: d, start_y: d) -> None:
        self._start_x = start_x
        self._start_y = start_y
        self._track = []

    def add_point(self, x: d, y: d, speed: d) -> None:
        """Добавление новой точки в маршрут."""
        self._track.append([(x, y), speed])

    def __getitem__(self, index: int):
        self._validate_index(index)
        return tuple(self._track[index])

    def __setitem__(self, key: int, value: d):
        self._validate_index(key)
        if not isinstance(value, (int, float)):
            raise ValueError
        self._track[key][1] = value

    def _validate_index(self, index: int) -> bool:
        if (
            not isinstance(index, int)
            or not -len(self._track) <= index <= len(self._track) - 1
        ):
            raise IndexError("некорректный индекс")
        return True


if __name__ == "__main__":
    tr = Track(10, -5.4)
    assert tr._start_x == 10 and tr._start_y == -5.4
    tr.add_point(20, 0, 100)  # первый линейный сегмент: indx = 0
    # assert tr._track == [((20, 0), 100)]
    tr.add_point(50, -20, 80)  # второй линейный сегмент: indx = 1
    # assert tr._track == [((20, 0), 100), ((50, -20), 80)]
    tr.add_point(63.45, 1.24, 60.34)  # третий линейный сегмент: indx = 2

    tr[2] = 60
    c, s = tr[0]
    print(c, s)

    try:
        res = tr[3]  # IndexError
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось исключение IndexError"
