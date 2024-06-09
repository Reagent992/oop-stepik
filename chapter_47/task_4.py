from typing import Callable, Optional, Type


class Descriptor:
    def __init__(
        self, validator: Optional[Callable] = None, exception=ValueError
    ) -> None:
        self.validator = validator
        self.exception = exception

    def __set_name__(self, owner: Type[object], name: str):
        self.private_name = f"_{name}"

    def __get__(self, obj: object, objtype=None):
        return getattr(obj, self.private_name, None)

    def __set__(self, obj: object, value) -> None:
        if self.validator is not None:
            if self.validator(value):
                setattr(obj, self.private_name, value)


def validator_name(value: str) -> bool:
    if not isinstance(value, str):
        raise ValueError
    return True


def validator_ton(value: int) -> bool:
    if not isinstance(value, int):
        raise ValueError
    if value not in (-1, 0, 1):
        raise ValueError
    return True


class Note:
    _name = Descriptor(validator_name)
    _ton = Descriptor(validator_ton)

    def __init__(self, name: str, ton: int = 0) -> None:
        self._name = name
        self._ton = ton


class Notes:
    __slots__ = ("_do", "_re", "_mi", "_fa", "_solt", "_la", "_si")
    __сyrillic_notes = ("до", "ре", "ми", "фа", "соль", "ля", "си")
    __obj = None

    def __new__(cls) -> "Notes":
        if not cls.__obj:
            cls.__obj = super().__new__(cls)
        return cls.__obj

    def __init__(self) -> None:
        for note, ru_name in zip(self.__slots__, self.__сyrillic_notes):
            setattr(self, note, Note(ru_name))

    def __getitem__(self, index: int) -> Note:
        self.validate_index(index)
        return getattr(self, self.__slots__[index])

    @classmethod
    def validate_index(cls, value: int) -> bool:
        if (
            not isinstance(value, int)
            or not 0 <= value <= len(cls.__slots__) - 1
        ):
            raise IndexError
        return True


if __name__ == "__main__":
    assert issubclass(Note, object)
    n = Note("a", 1)
    assert hasattr(n, "_name")
    assert hasattr(n, "_ton")
    args = ((1, -2), ("a", 2), ("a", 0.1), ("a", 4))
    for i in args:
        try:
            Note(*i)  # type: ignore
        except ValueError:
            assert True
        else:
            assert False
    try:
        n._ton = 10
    except ValueError:
        assert True
    else:
        assert False
    try:
        n._ton = 100
    except ValueError:
        assert True
    else:
        assert False

    assert issubclass(Notes, object)
    assert hasattr(Notes, "__slots__")
    nts = Notes()
    nts2 = Notes()
    assert id(nts) == id(nts2)
    for attr in Notes.__slots__:
        assert hasattr(nts, attr)
    for index, note in enumerate(Notes.__slots__):
        assert nts[index] == getattr(nts, note)
    wrong_indexes = (-1, len(Notes.__slots__), 0.1)
    for wrong_index in wrong_indexes:
        try:
            nts[wrong_index]  # type: ignore
        except IndexError:
            assert True
        else:
            assert False
    old_tone = nts[0]._ton
    nts[0]._ton = -1
    assert nts[0] != old_tone
