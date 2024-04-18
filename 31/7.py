from typing import Any, Union


numbers = Union[int, float]


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def __init__(self, a: numbers, b: numbers, c: numbers) -> None:
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def c(self):
        return self.__c

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name in ("MIN_DIMENSION", "MAX_DIMENSION"):
            raise AttributeError(
                "Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено."
            )
        elif __name in ("_Dimensions__a", "_Dimensions__b", "_Dimensions__c"):
            if (
                isinstance(__value, (int, float))
                and self.MIN_DIMENSION <= __value <= self.MAX_DIMENSION
            ):
                super().__setattr__(__name, __value)


# TEST-TASK___________________________________
x = Dimensions(10.0, 20, 30)
# проверка что в классе прописаны объекты свойства a-b-c
assert (
    type(Dimensions.a) is property
), "a - не является объектом свойством property"
assert (
    type(Dimensions.b) is property
), "b - не является объектом свойством property"
assert (
    type(Dimensions.c) is property
), "c - не является объектом свойством property"

# проверка что в объекте класса существуют 3 приватных локальных атрибута
assert (
    "_Dimensions__a" in x.__dict__
    and "_Dimensions__b" in x.__dict__
    and "_Dimensions__c" in x.__dict__
), "атрибуты не являются приватными"
# проверка что данные считываются с приватных атрибутов
assert (
    x.a == 10.0 and x.b == 20 and x.c == 30
), "при обращении к приватным атрибутам значения не получены проверьте объекты свойства"
# проверка что значения являются целым или вещественным числами
assert (
    type(x.a) in (int, float)
    and type(x.b) in (int, float)
    and type(x.c) in (int, float)
), "значения должны быть или целым числом или вещественным"
# проверка на существование атрибутов минимум-максимум
assert hasattr(x, "MIN_DIMENSION"), "не найден атрибут MIN_DIMENSION"
assert hasattr(x, "MAX_DIMENSION"), "не найден атрибут MAX_DIMENSION"

# проверка что значение в диапазоне
x.a = 9
assert (
    x.a == 10.0
), "присваиваемое значение должно быть в диапазоне [MIN_DIMENSION; MAX_DIMENSION]"
x.b = -1
assert (
    x.b == 20
), "присваиваемое значение должно быть в диапазоне [MIN_DIMENSION; MAX_DIMENSION]"
x.c = 1001
assert (
    x.c == 30
), "присваиваемое значение должно быть в диапазоне [MIN_DIMENSION; MAX_DIMENSION]"

# проверка
# С помощью магических методов данного занятия запретить создание локальных атрибутов MIN_DIMENSION и MAX_DIMENSION в объектах класса Dimensions.
# При попытке это сделать генерировать исключение:
# raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
try:
    x.MIN_DIMENSION = 0
except AttributeError:
    assert True
else:
    assert False, "не сгенерировалось исключение AttributeError"

try:
    x.MAX_DIMENSION = 0
except AttributeError:
    assert True
else:
    assert False, "не сгенерировалось исключение AttributeError"

assert (
    "MIN_DIMENSION" not in x.__dict__
), "запретить создание локальных атрибутов MIN_DIMENSION и MAX_DIMENSION в объектах класса Dimensions"
assert (
    "MAX_DIMENSION" not in x.__dict__
), "запретить создание локальных атрибутов MIN_DIMENSION и MAX_DIMENSION в объектах класса Dimensions"
print("Прекрасный ответ !")
