from typing import Tuple, Union


Digits = Union[int, float]


class TrackLine:
    """Линейный сегмент маршрута."""

    def __init__(self, to_x: Digits, to_y: Digits, max_speed: int = 0) -> None:
        self.to_x = to_x
        self.to_y = to_y
        self.__max_speed = max_speed

    def get_track(self) -> Tuple[Digits, Digits]:
        """Получение координат линейного сегмента."""
        return self.to_x, self.to_y

    @property
    def x(self):
        return self.to_x

    @property
    def y(self):
        return self.to_y

    @property
    def max_speed(self):
        return self.__max_speed


class Track:
    """Маршрут."""

    def __init__(self, start_x: Digits = 0, start_y: Digits = 0) -> None:
        self.validate_digits(start_x, start_y)
        self.__start_x = start_x
        self.__start_y = start_y
        self.__track = []

    def add_track(self, tr: TrackLine) -> None:
        """Добавление линейного сегмента маршрута (следующей точки)."""
        self.__track.append(tr)

    def get_tracks(self) -> Tuple[TrackLine, ...]:
        return tuple(self.__track)

    @staticmethod
    def validate_digits(*values: Digits) -> bool:
        if all(isinstance(value, (int, float)) for value in values):
            return True
        raise ValueError("Неверный тип данных.")

    def __len__(self):
        len_1 = (
            (self.__start_x - self.__track[0].x) ** 2
            + (self.__start_y - self.__track[0].y) ** 2
        ) ** 0.5
        return int(
            len_1
            + sum(self.__get_length(i) for i in range(1, len(self.__track)))
        )

    def __get_length(self, i):
        return (
            (self.__track[i - 1].x - self.__track[i].x) ** 2
            + (self.__track[i - 1].y - self.__track[i].y) ** 2
        ) ** 0.5

    def __eq__(self, __value: TrackLine) -> bool:
        return len(self) == len(__value)

    def __lt__(self, __value):
        return len(self) < len(__value)


track1, track2 = Track(), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2
