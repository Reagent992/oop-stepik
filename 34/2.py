from typing import Any, List, Union


class Descriptor:

    def __set_name__(self, owner, name: str):
        self.private_name = f"_{owner.__name__}__{name}"

    def __get__(self, obj: object, objtype=None) -> List[Union[int, float]]:
        return getattr(obj, self.private_name)

    def __set__(self, obj: object, value) -> None:
        setattr(obj, self.private_name, self.validate(value))

    def validate(self, value: List[Any]) -> List[Union[int, float]]:
        return [i for i in value if type(i) in (int, float)]


class ListMath:
    lst_math = Descriptor()

    def __init__(self, list_: List[Any] = []) -> None:
        self.lst_math: List[Union[int, float]] = list_  # type: ignore

    # -----------------------------------------------------------------Сложение
    def __add__(self, value: Union[int, float]) -> "ListMath":
        if self.validate(value):
            return ListMath([i + value for i in self.lst_math])
        return self

    def __radd__(self, value: Union[int, float]) -> "ListMath":
        return self + value

    def __iadd__(self, value: Union[int, float]) -> "ListMath":
        self.lst_math = [i + value for i in self.lst_math]
        return self

    # ----------------------------------------------------------------Вычитание
    def __sub__(self, value: Union[int, float]) -> "ListMath":
        if self.validate(value):
            return ListMath([i - value for i in self.lst_math])
        return self

    def __rsub__(self, value: Union[int, float]) -> "ListMath":
        if self.validate(value):
            return ListMath([value - i for i in self.lst_math])
        return self

    def __isub__(self, value: Union[int, float]) -> "ListMath":
        self.lst_math = [i - value for i in self.lst_math]
        return self

    # ----------------------------------------------------------------Умножение
    def __mul__(self, value: Union[int, float]) -> "ListMath":
        if self.validate(value):
            return ListMath([i * value for i in self.lst_math])
        return self

    def __rmul__(self, value: Union[int, float]) -> "ListMath":
        return self * value

    def __imul__(self, value: Union[int, float]) -> "ListMath":
        self.lst_math = [i * value for i in self.lst_math]
        return self

    # ------------------------------------------------------------------Деление
    def __truediv__(self, value: Union[int, float]) -> "ListMath":
        if self.validate(value):
            return ListMath([i / value for i in self.lst_math])
        return self

    def __rtruediv__(self, value: Union[int, float]) -> "ListMath":
        return self / value

    def __itruediv__(self, value: Union[int, float]) -> "ListMath":
        self.lst_math = [i / value for i in self.lst_math]
        return self

    @staticmethod
    def validate(value) -> bool:
        return type(value) in (int, float)


if __name__ == "__main__":
    # Создание.
    lst = ListMath([1, "abc", -5, 7.68, True])
    assert lst.lst_math == [1, -5, 7.68]
    # -------------------------------------------------------------------------
    # Сложение.
    add_lst = lst + 2
    assert add_lst.lst_math == [3, -3, 9.68]
    # "Обратное" сложение.
    rev_add_lst = 2 + lst
    assert rev_add_lst.lst_math == [3, -3, 9.68]
    # "Короткое" сложение.
    lst += 2
    assert lst.lst_math == [3, -3, 9.68]
    lst = ListMath([1, "abc", -5, 7.68, True])  # откат
    # -------------------------------------------------------------------------
    # Вычитание.
    sub_lst = lst - 2
    assert sub_lst.lst_math == [-1, -7, 5.68]
    # "Обратное" вычитание.
    rev_sub_lst = 2 - lst
    assert rev_sub_lst.lst_math == [1, 7, -5.68]
    # "Короткое" вычитание.
    lst -= 2
    assert lst.lst_math == [-1, -7, 5.68]
    lst = ListMath([1, "abc", -5, 7.68, True])  # откат
    # -------------------------------------------------------------------------
    # Умножение.
    mul_lst = lst * 2
    assert mul_lst.lst_math == [2, -10, 15.36]
    # "Обратное" умножение.
    rev_mul_lst = 2 * lst
    assert rev_mul_lst.lst_math == [2, -10, 15.36]
    # "Короткое" умножение.
    lst *= 2
    assert lst.lst_math == [2, -10, 15.36]
    lst = ListMath([1, "abc", -5, 7.68, True])  # откат
    # -------------------------------------------------------------------------
    # Деление.
    t = ListMath([1, 2, 4])
    div_t = t / 2
    assert div_t.lst_math == [0.5, 1, 2]
    # Обратное деление.
    rev_div_t = 2 / t
    assert rev_div_t.lst_math == [0.5, 1, 2]
    # "Короткое" деление.
    t /= 2
    assert t.lst_math == [0.5, 1, 2]
    # -------------------------------------------------------------------------
