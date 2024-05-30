# здесь объявляйте декоратор и все что с ним связано
from typing import Callable, List


def log_decorator(func: Callable, lst: List):
    def wrapper(*args, **kwargs):
        lst.append(func.__name__)
        return func(*args, **kwargs)

    return wrapper


def class_log(decorator_args) -> Callable:
    def inner_class_log(cls):
        def wrapper(*args, **kwargs):
            methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
            for k, v in methods.items():
                setattr(cls, k, log_decorator(v, decorator_args))
            return cls(*args, **kwargs)

        return wrapper

    return inner_class_log


vector_log = []  # наименование (vector_log) в программе не менять!


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

if __name__ == '__main__':
    v = Vector(1, 2, 3)
    v[0] = 10
    print(vector_log)