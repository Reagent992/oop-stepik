from typing import Any, Dict, Tuple, Type


class Descriptor:
    def __set_name__(self, owner: Type[object], name: str):
        self.private_name = f"_{owner.__name__}__{name}"

    def __get__(self, obj: object, objtype=None):
        return getattr(obj, self.private_name, None)

    def __set__(self, obj: object, value) -> None:
        if self.validate(value):
            setattr(obj, self.private_name, value)

    def validate(self, value) -> bool:
        if not isinstance(value, int):
            raise ValueError("Wrong type of value passed. Int's only.")
        return True


class Cell:
    def __init__(self, value: Any) -> None:
        self.value = value

    def __str__(self) -> str:
        return self.value


class SparseTable:
    rows = Descriptor()
    cols = Descriptor()

    def __init__(self, rows: int = 0, cols: int = 0) -> None:
        self.rows = rows
        self.cols = cols
        self._stash: Dict[Tuple[int, int], Cell] = {}

    def add_data(self, row: int, col: int, data: Any) -> None:
        """Добавление данных в таблицу по индексам."""
        self.validate_row_col(row, col)
        if not isinstance(data, Cell):
            data = Cell(data)
        self._stash[(row, col)] = data

    def remove_data(self, row: int, col: int) -> None:
        """Удаление ячейки по индексу."""
        if self._stash.get((row, col)) is None:
            raise IndexError("ячейка с указанными индексами не существует")
        del self._stash[(row, col)]
        if row + 1 == self.rows:
            self.rows = row
        if col + 1 == self.cols:
            self.cols = col - 1

    def __getitem__(self, index: Tuple[int, int]) -> Cell:
        self.validate_row_col(*index)
        if self._stash.get(index) is None:
            raise ValueError("данные по указанным индексам отсутствуют")
        return self._stash[index].value

    def __setitem__(self, index: Tuple[int, int], value: Any) -> None:
        self.validate_row_col(*index)
        if not isinstance(value, Cell):
            value = Cell(value)
        self._stash[index] = value

    def validate_row_col(self, row: int, col: int) -> bool:
        if not isinstance(row, int) or not isinstance(col, int):
            raise ValueError("Wrong type of value passed")
        if not 0 <= row or not 0 <= col:
            raise IndexError("Wrong index passed")
        if row > self.rows - 1:
            self.rows = row + 1
        if col > self.cols - 1:
            self.cols = col + 1
        return True


if __name__ == "__main__":
    # Cell
    c1 = Cell("1")
    c2 = Cell("2")
    c3 = Cell("3")

    # SparseTable
    st1 = SparseTable(3, 3)
    assert st1._stash == {}
    # add to table
    st1.add_data(0, 0, c1)
    st1.add_data(2, 2, c1)

    # get value by index
    assert st1[0, 0] == c1.value
    assert st1[2, 2] == c1.value

    # set by index
    st1[0, 2] = c2
    assert st1[0, 2] == c2.value
    st1[0, 2] = "abc"
    assert st1[0, 2] == "abc"
    # remove
    st1.remove_data(0, 0)
    try:
        st1.remove_data(0, 0)
    except IndexError:
        assert True
    else:
        assert False, "Must be IndexError"

    st = SparseTable()
    st.add_data(2, 5, Cell(25))
    st.add_data(1, 1, Cell(11))
    assert (
        st.rows == 3 and st.cols == 6
    ), "неверные значения атрибутов rows и cols"

    try:
        v = st[3, 2]
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError"

    st[3, 2] = 100
    assert (
        st[3, 2] == 100
    ), "неверно отработал оператор присваивания нового значения в ячейку таблицы"
    assert (
        st.rows == 4 and st.cols == 6
    ), "неверные значения атрибутов rows и cols"

    st[4, 7] = 132
    assert (
        st.rows == 5 and st.cols == 8
    ), "неверные значения атрибутов rows и cols"

    st.remove_data(4, 7)
    assert (
        st.rows == 4 and st.cols == 6
    ), "неверные значения атрибутов rows и cols, возможно, некорректно отработал метод remove_data"

    st.remove_data(1, 1)
    try:
        v = st[1, 1]
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError"

    try:
        st.remove_data(1, 1)
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось исключение IndexError"

    d = Cell("5")
    assert (
        d.value == "5"
    ), "неверное значение атрибута value в объекте класса Cell, возможно, некорректно работает инициализатор класса"
