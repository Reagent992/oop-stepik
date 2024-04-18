from typing import Union


class Body:
    def __init__(
        self,
        name: str,
        ro: Union[int, float],
        volume: Union[int, float],
    ) -> None:
        self.__name = name
        self.__ro = ro
        self.__volume = volume

    def get_mass(self):
        return self.__ro * self.__volume

    def __lt__(self, value: Union["Body", int, float]) -> bool:
        if isinstance(value, Body):
            return self.get_mass() < value.get_mass()
        elif isinstance(value, (int, float)):
            return self.get_mass() < value

    def __gt__(self, value: Union["Body", int, float]) -> bool:
        if isinstance(value, Body):
            return self.get_mass() > value.get_mass()
        elif isinstance(value, (int, float)):
            return self.get_mass() > value

    def __eq__(self, value: Union["Body", int, float]) -> bool:  # type: ignore
        if isinstance(value, Body):
            return self.get_mass() == value.get_mass()
        elif isinstance(value, (int, float)):
            return self.get_mass() == value


if __name__ == "__main__":
    b1 = Body("abc", 10, 10)
    b2 = Body("abc", 10, 10)
    assert (b1 == b2) is True

    b3 = Body("asdas", 100, 100)
    assert (b1 < b3) is True

    assert (b1 < 1000) is True
    assert (b1 > 1000) is False
