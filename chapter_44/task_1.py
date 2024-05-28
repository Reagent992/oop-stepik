from typing import Any, Type, Union


class Descriptor:
    def __init__(self, validate_type, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.validate_type = validate_type

    def __set_name__(self, owner: Type[object], name: str) -> None:
        self.private_name = f"_{owner.__name__}__{name}"

    def __get__(self, obj: object, objtype=None) -> Union[Any, None]:
        return getattr(obj, self.private_name, None)

    def __set__(self, obj: object, value) -> None:
        if self.validate(value):
            setattr(obj, self.private_name, value)

    def validate(self, value) -> bool:
        if not isinstance(value, self.validate_type):
            raise TypeError
        return True


class Animal:
    name = Descriptor(str)
    kind = Descriptor(str)
    old = Descriptor(int)

    def __init__(self, name: str, kind: str, old: int) -> None:
        self.name = name
        self.kind = kind
        self.old = old


animals = [
    Animal("Васька", "дворовый кот", 5),
    Animal("Рекс", "немецкая овчарка", 8),
    Animal("Кеша", "попугай", 3),
]

if __name__ == "__main__":
    animal = Animal("abc", "woolf", 10)
    assert animal.name == "abc"
    assert animal.kind == "woolf"
    assert animal.old == 10
    animal.old = 50
    assert animal.old == 50
    animal.name = "vasya"
    assert animal.name == "vasya"
    try:
        animal.old = "abc"
    except TypeError:
        assert True
    else:
        assert False
