from typing import Any, Callable, Type


def integer_params_decorated(func: Callable) -> Callable:
    def wrapper(self, *args, **kwargs) -> Callable:
        if not all(isinstance(i, int) for i in args):
            raise TypeError("аргументы должны быть целыми числами")
        if kwargs:
            if not all(type(i) == type(int) for i in kwargs.keys()):
                raise TypeError("аргументы должны быть целыми числами")
        result = func(self, *args, **kwargs)
        return result

    return wrapper


def integer_params(cls: Type["Vector"]) -> Type["Vector"]:
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))

    return cls


@integer_params
class Vector:
    def __init__(self, *args) -> None:
        self.__coords = list(args)

    def __getitem__(self, item) -> Any:
        return self.__coords[item]

    def __setitem__(self, key, value) -> None:
        self.__coords[key] = value

    def set_coords(self, *coords, reverse=False) -> None:
        c = list(coords)
        self.__coords = c if not reverse else c[::-1]


if __name__ == "__main__":
    vector = Vector(1, 2)
    print(vector[1])
    try:
        vector[1] = 20.4  # TypeError
    except TypeError:
        assert True
    else:
        assert False
    try:
        vector.set_coords(1, 2, reverse=True)
    except TypeError:
        assert True
    else:
        assert False
