from typing import Dict, Type, Union

Digit = Union[int, float]


class Descriptor:
    def __init__(self, required_type) -> None:
        self.required_type = required_type

    def __set_name__(self, owner: Type[object], name: str):
        self.private_name = f"_{owner.__name__}__{name}"

    def __get__(self, obj: object, objtype=None):
        return getattr(obj, self.private_name, None)

    def __set__(self, obj: object, value) -> None:
        if self.validate(value):
            setattr(obj, self.private_name, value)

    def validate(self, value) -> bool:
        if not isinstance(value, self.required_type):
            raise TypeError
        if type(self.required_type) == tuple:
            if (
                any(i in (int, float) for i in self.required_type)
                and not value > 0
            ):
                raise TypeError
        if self.required_type in (int, float) and not value > 0:
            raise TypeError
        return True


class Aircraft:
    _model = Descriptor(str)
    _mass = Descriptor((int, float))
    _top = Descriptor((int, float))
    _speed = Descriptor((int, float))

    def __init__(
        self, model: str, mass: Digit, speed: Digit, top: Digit
    ) -> None:
        self._model = model
        self._mass = mass
        self._top = top
        self._speed = speed


class PassengerAircraft(Aircraft):
    _chairs = Descriptor(int)

    def __init__(
        self, model: str, mass: Digit, speed: Digit, top: Digit, chairs: int 
    ) -> None:
        super().__init__(model, mass, speed, top)
        self._chairs = chairs


class WarPlane(Aircraft):
    _weapons = Descriptor(dict)

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
