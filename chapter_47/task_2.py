from typing import Union


Digits = Union[int, float]


class Planet:
    def __init__(
        self, name: str, diametr: Digits, period_solar: Digits, period: Digits
    ) -> None:
        self._name = name
        self._diametr = diametr
        self._period_solar = period_solar
        self._period = period


class SolarSystem:
    __obj = None

    def __new__(cls):
        if not cls.__obj:
            cls.__obj = super().__new__(cls)
        return cls.__obj

    def __init__(self) -> None:
        self._mercury = Planet("Меркурий", 4878, 87.97, 1407.5)
        self._venus = Planet("Венера", 12104, 224.7, 5832.45)
        self._earth = Planet("Земля", 12756, 365.3, 23.93)
        self._mars = Planet("Марс", 6794, 687, 24.62)
        self._jupiter = Planet("Юпитер", 142800, 4330, 9.9)
        self._saturn = Planet("Сатурн", 120660, 10753, 10.63)
        self._uranus = Planet("Уран", 51118, 30665, 17.2)
        self._neptune = Planet("Нептун", 49528, 60150, 16.1)

    __slots__ = (
        "_mercury",
        "_venus",
        "_earth",
        "_mars",
        "_jupiter",
        "_saturn",
        "_uranus",
        "_neptune",
    )


s_system = SolarSystem()

if __name__ == "__main__":
    assert issubclass(Planet, object)
    p = Planet("name", 1, 2, 3)
    assert hasattr(p, "_name")
    assert hasattr(p, "_diametr")
    assert hasattr(p, "_period_solar")
    assert hasattr(p, "_period")

    assert issubclass(SolarSystem, object)
    assert hasattr(SolarSystem, "__slots__")
    assert SolarSystem.__slots__ == (
        "_mercury",
        "_venus",
        "_earth",
        "_mars",
        "_jupiter",
        "_saturn",
        "_uranus",
        "_neptune",
    )
    s1 = SolarSystem()
    s2 = SolarSystem()
    assert id(s1) == id(s2)
    for i in (
        "_mercury",
        "_venus",
        "_earth",
        "_mars",
        "_jupiter",
        "_saturn",
        "_uranus",
        "_neptune",
    ):
        assert hasattr(s1, i)
    assert isinstance(s_system, SolarSystem)
