from typing import Callable, Dict, Type, Union

Digit = Union[int, float]


def digits_validator(value: Digit) -> bool:
    if not isinstance(value, (int, float)) or value <= 0:
        raise TypeError
    return True


def str_validator(value: str) -> bool:
    if not isinstance(value, str):
        raise TypeError
    return True


def dict_validator(value: dict) -> bool:
    if not isinstance(value, dict):
        raise TypeError
    return True


def int_validator(value: int) -> bool:
    if not isinstance(value, int):
        raise TypeError
    return True


class Descriptor:
    def __init__(self, validator: Callable) -> None:
        self.validator = validator

    def __set_name__(self, owner: Type[object], name: str):
        self.private_name = f"_{owner.__name__}__{name}"

    def __get__(self, obj: object, objtype=None):
        return getattr(obj, self.private_name, None)

    def __set__(self, obj: object, value) -> None:
        if self.validator(value):
            setattr(obj, self.private_name, value)


class Aircraft:
    _model = Descriptor(str_validator)
    _mass = Descriptor(digits_validator)
    _top = Descriptor(digits_validator)
    _speed = Descriptor(digits_validator)

    def __init__(
        self, model: str, mass: Digit, speed: Digit, top: Digit
    ) -> None:
        self._model = model
        self._mass = mass
        self._top = top
        self._speed = speed


class PassengerAircraft(Aircraft):
    _chairs = Descriptor(int_validator)

    def __init__(
        self, model: str, mass: Digit, speed: Digit, top: Digit, chairs: int
    ) -> None:
        super().__init__(model, mass, speed, top)
        self._chairs = chairs


class WarPlane(Aircraft):
    _weapons = Descriptor(dict_validator)

    def __init__(
        self,
        model: str,
        mass: Digit,
        speed: Digit,
        top: Digit,
        weapons: Dict[str, int],
    ) -> None:
        super().__init__(model, mass, speed, top)
        self._weapons = weapons


planes = [
    PassengerAircraft("МС-21", 1250, 8000, 12000.5, 140),
    PassengerAircraft("SuperJet", 1145, 8640, 11034, 80),
    WarPlane("Миг-35", 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
    WarPlane("Су-35", 7034, 34000, 2400, {"ракета": 4, "бомба": 7}),
]
if __name__ == "__main__":
    Aircraft("a", 1, 2, 3)
    array = (("4", 1, -2, 3), (1, 2, 3, 4))
    for i in array:
        try:
            Aircraft(*i)
        except TypeError:
            assert True
        else:
            assert False
