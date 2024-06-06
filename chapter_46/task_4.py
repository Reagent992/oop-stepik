from typing import Union


class MoneyOperators:
    def __add__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money + other)

        if type(self) != type(other):
            raise TypeError("Разные типы объектов")

        return self.__class__(self.money + other.money)

    # здесь объявляйте еще один метод
    def __sub__(self, value):
        if isinstance(value, (int, float)):
            return self.__class__(self.money - value)
        if type(self) != type(value):
            raise TypeError("Разные типы объектов")
        return self.__class__(self.money - value.money)


# здесь объявляйте класс Money
class Money:
    def __init__(self, value: Union[int, float]) -> None:
        self.money = value

    @property
    def money(self) -> Union[int, float]:
        return self._money

    @money.setter
    def money(self, value: Union[int, float]) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError
        self._money = value


class MoneyR(Money, MoneyOperators):
    def __str__(self) -> str:
        return f"MoneyR: {self.money}"


class MoneyD(Money, MoneyOperators):
    def __str__(self) -> str:
        return f"MoneyD: {self.money}"


if __name__ == "__main__":
    assert issubclass(Money, object)
    m = Money(10)
    assert hasattr(m, "_money")
    assert m._money == 10

    try:
        Money("a")  # type: ignore
    except TypeError:
        assert True
    else:
        assert False
