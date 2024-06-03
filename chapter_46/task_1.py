from typing import Any, Union


def validator(value: Any, required_type: Any) -> bool:
    if not isinstance(value, required_type):
        raise TypeError
    return True


class Digit:
    def __init__(self, value: Union[int, float]) -> None:
        validator(value, (int, float))
        self.value = value


class Integer(Digit):
    def __init__(self, value: int) -> None:
        validator(value, int)
        super().__init__(value)


class Float(Digit):
    def __init__(self, value: float) -> None:
        validator(value, float)
        super().__init__(value)


class Negative(Digit):
    def __init__(self, value: Union[int, float]) -> None:
        if not value < 0:
            raise TypeError
        super().__init__(value)


class Positive(Digit):
    def __init__(self, value: Union[int, float]) -> None:
        if not value > 0:
            raise TypeError
        super().__init__(value)


class PrimeNumber(Positive, Integer): ...


class FloatPositive(Positive, Float): ...


o1 = PrimeNumber(1)
o2 = PrimeNumber(2)
o3 = PrimeNumber(3)
fp1 = FloatPositive(0.5)
fp2 = FloatPositive(0.6)
fp3 = FloatPositive(0.7)
fp4 = FloatPositive(0.8)
fp5 = FloatPositive(0.9)
digits = [
    o1,
    o2,
    o3,
    fp1,
    fp2,
    fp3,
    fp4,
    fp5,
]
lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))
if __name__ == "__main__":
    assert issubclass(Digit, object)
    d = Digit(1)
    assert d.value == 1
    assert issubclass(Integer, Digit)
    i = Integer(1)
    assert i.value == 1
    assert issubclass(Float, Digit)
    f = Float(0.5)
    assert f.value == 0.5
    assert issubclass(Positive, Digit)
    p = Positive(20)
    assert p.value == 20
    assert issubclass(Negative, Digit)
    n = Negative(-1)
    assert n.value == -1
    assert issubclass(PrimeNumber, Integer) and issubclass(
        PrimeNumber, Positive
    )
    pn = PrimeNumber(10)
    assert pn.value == 10
    assert issubclass(FloatPositive, Float) and issubclass(
        FloatPositive, Positive
    )
    fails = (
        (Digit, "a"),
        (Integer, 0.4),
        (Float, 1),
        (Positive, -1),
        (Negative, 1),
        (PrimeNumber, -0.5),
        (FloatPositive, -1),
    )
    for fail in fails:
        try:
            fail[0](fail[1])  # type: ignore
        except TypeError:
            assert True
        else:
            assert False

    assert lst_positive == [o1, o2, o3, fp1, fp2, fp3, fp4, fp5]
    assert lst_float == [fp1, fp2, fp3, fp4, fp5]
