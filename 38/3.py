from typing import Any, Type


class Array:
    def __init__(self, max_length: int, cell: Type[Any]) -> None:
        self._max_length = max_length
        self._type = cell
        self._array = [cell() for _ in range(max_length)]

    def __getitem__(self, item: int) -> int:
        """Получение значения элемента массива по индексу."""
        self.validate_index(item)
        self.validate_obj_has_attr(item, "value")
        return self._array[item].value

    def __setitem__(self, key: int, value: Any) -> None:
        """Установка нового значения в ячейку массива по индексу."""
        self.validate_index(key)
        self.validate_obj_has_attr(key, "value")
        self._array[key].value = value

    def __str__(self) -> str:
        return " ".join(str(i.value) for i in self._array)

    def validate_index(self, index: int) -> bool:
        if (
            not isinstance(index, int)
            or not -self._max_length <= index <= self._max_length - 1
        ):
            raise IndexError("неверный индекс для доступа к элементам массива")
        return True

    def validate_obj_has_attr(self, obj: Any, attr: str) -> bool:
        if not hasattr(self._array[obj], attr):
            raise AttributeError
        return True


class Integer:
    def __init__(self, start_value: int = 0) -> None:
        self.__value = start_value

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, new_value: int) -> None:
        if not isinstance(new_value, int):
            raise ValueError("должно быть целое число")
        self.__value = new_value


class Float:
    def __init__(self, start_value: float = 0) -> None:
        self.__start_value = start_value

    @property
    def value(self) -> float:
        return self.__start_value

    @value.setter
    def value(self, value: float) -> None:
        if not isinstance(value, float):
            raise ValueError("должно быть целое число")
        self.__start_value = value


float_array = Array(3, Float)

if __name__ == "__main__":
    # Array creation
    array_1 = Array(3, Integer)
    assert array_1._max_length == 3 and array_1._type == Integer

    # Integer creation
    int_1 = Integer(10)
    assert int_1.value == 10
    int_1.value = 20
    assert int_1.value == 20
    try:
        int_1.value = 0.01  # type: ignore
    except ValueError:
        assert True
    else:
        assert False, "must be: raise ValueError"

    # Get int from array
    assert array_1[0] == 0 and array_1[1] == 0 and array_1[2] == 0
    assert array_1[-1] == 0 and array_1[-2] == 0 and array_1[-3] == 0
    for index in (3, -4):
        try:
            array_1[index]
        except IndexError:
            assert True
        else:
            assert False, "must be: raise IndexError"

    # Set int to array
    array_1[1] = 22
    assert array_1[1] == 22 and array_1[-2] == 22
    for index in (3, -4):
        try:
            array_1[index] = 100500
        except IndexError:
            assert True
        else:
            assert False, "must be: raise IndexError"

    assert str(array_1) == "0 22 0"

    # Float
    float_1 = Float(0.01)
    assert float_1.value == 0.01
    float_1.value = 0.02
    assert float_1.value == 0.02
    try:
        float_1.value = 10  # type: ignore
    except ValueError:
        assert True
    else:
        assert False, "must be: raise ValueError"

    # Float array
    array_1 = Array(3, Float)

    # Get float from empty array
    assert array_1[0] == 0 and array_1[1] == 0 and array_1[2] == 0
    assert array_1[-1] == 0 and array_1[-2] == 0 and array_1[-3] == 0
    for index in (3, -4):
        try:
            array_1[index]
        except IndexError:
            assert True
        else:
            assert False, "must be: raise IndexError"

    # Set float to array
    array_1[1] = 0.01
    assert array_1[1] == 0.01 and array_1[-2] == 0.01
    for index in (3, -4):
        try:
            array_1[index] = 0.01
        except IndexError:
            assert True
        else:
            assert False, "must be: raise IndexError"

    assert str(array_1) == "0 0.01 0"
