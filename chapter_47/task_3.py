from typing import Union


class Star:
    __slots__ = ("_name", "_massa", "_temp")

    def __init__(
        self, name: str, massa: Union[int, float], temp: Union[int, float]
    ) -> None:
        self._name = name
        self._massa = massa
        self._temp = temp


class StarMixin(Star):
    __slots__ = ("_type_star", "_radius")

    def __init__(
        self,
        name: str,
        massa: Union[int, float],
        temp: Union[int, float],
        type_star: str,
        radius: Union[int, float],
    ) -> None:
        super().__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius


class WhiteDwarf(StarMixin):
    __slots__ = ()


class YellowDwarf(StarMixin):
    __slots__ = ()


class RedGiant(StarMixin):
    __slots__ = ()


class Pulsar(StarMixin):
    __slots__ = ()


stars = [
    RedGiant("Альдебаран", 5, 3600, "красный гигант", 45),
    WhiteDwarf("Сириус А", 2.1, 9250, "белый карлик", 2),
    WhiteDwarf("Сириус B", 1, 8200, "белый карлик", 0.01),
    YellowDwarf("Солнце", 1, 6000, "желтый карлик", 1),
]
white_dwarfs = list(filter(lambda x: isinstance(x, WhiteDwarf), stars))
if __name__ == "__main__":
    assert issubclass(Star, object)
    assert hasattr(Star, "__slots__")
    assert Star.__slots__ == ("_name", "_massa", "_temp")
    s = Star("a", 1, 2)
    assert hasattr(s, "_name")
    assert hasattr(s, "_massa")
    assert hasattr(s, "_temp")

    assert issubclass(WhiteDwarf, Star)
    assert issubclass(YellowDwarf, Star)
    assert issubclass(RedGiant, Star)
    assert issubclass(Pulsar, Star)
    # for i in (WhiteDwarf, YellowDwarf, RedGiant, Pulsar):
    #     assert i.__slots__ == ("_type_star", "_radius")
    assert stars
    assert white_dwarfs
