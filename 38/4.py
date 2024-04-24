from typing import Any, Optional, Tuple, Type


class IntegerValue:
    """Дескриптор данных для работы с целыми числами."""

    def __set_name__(self, owner: Type[object], name: str):
        self.private_name = f"_{owner.__name__}__{name}"

    def __get__(self, obj: object, objtype=None):
        return getattr(obj, self.private_name, None)

    def __set__(self, obj: object, value) -> None:
        if not self.validate(value):
            raise ValueError
        setattr(obj, self.private_name, value)

    def validate(self, value) -> bool:
        return isinstance(value, int)


class CellInteger:
    """Операций с целыми числами."""

    value = IntegerValue()

    def __init__(self, start_value: int = 0) -> None:
        self.value = start_value


class TableValues:
    """Работы с таблицей."""

    def __init__(self, row: int, cols: int, cell: Any = None) -> None:
        """
        Parameters:
        row (int):  число строк
        cols (int): число столбцов
        cell (Any):  ссылка на класс, описывающий
        работу с отдельными ячейками таблицы
        """
        if cell:
            self.cell = cell
        else:
            raise ValueError("параметр cell не указан")
        self.row = row
        self.cols = cols
        self.cells = tuple(
            tuple(cell() for _ in range(cols)) for _ in range(row)
        )

    def __getitem__(self, indexes: Tuple[int, int]) -> int:
        row_index, col_index = indexes
        self.validate_index_exist(row_index, col_index)
        obj = self.cells[row_index][col_index]
        if hasattr(obj, "value"):
            return obj.value
        else:
            raise TypeError

    def __setitem__(self, indexes: Tuple[int, int], value: int) -> None:
        row_index, col_index = indexes
        self.validate_index_exist(row_index, col_index)
        obj = self.cells[row_index][col_index]
        if hasattr(obj, "value"):
            obj.value = value
        else:
            raise TypeError

    def validate_index_exist(
        self, row_index: Optional[int] = None, col_index: Optional[int] = None
    ) -> bool:
        if row_index:
            if not -len(self.cells) <= row_index <= len(self.cells) - 1:
                raise IndexError
        if row_index and col_index:
            if (
                not -len(self.cells[row_index])
                <= col_index
                <= len(self.cells[row_index]) - 1
            ):
                raise IndexError
        return True


if __name__ == "__main__":
    # CellInteger
    c1 = CellInteger()
    assert c1.value == 0
    c1.value = 10
    assert c1.value == 10
    try:
        c1.value = 0.01
    except ValueError:
        assert True
    else:
        assert False

    # TableValues
    t1 = TableValues(2, 3, CellInteger)
    assert t1.row == 2
    assert t1.cols == 3
    # cells arg
    assert len(t1.cells) == 2
    for table_row in t1.cells:
        assert isinstance(table_row, tuple)
        assert len(table_row) == 3
        prev_obj = None
        for obj in table_row:
            assert isinstance(obj, CellInteger)
            if prev_obj:
                assert id(obj) != id(prev_obj)
            prev_obj = obj
    # raise
    try:
        TableValues(2, 2)
    except ValueError:
        assert True
    else:
        assert False, "should be raise ValueError"
    # indexes
    assert t1[0, 0] == 0
    t1[0, 0] = 1
    assert t1[0, 0] == 1
    try:
        t1[0, 0] = 0.01  # type: ignore
    except ValueError:
        assert True
    else:
        assert False, "must be raise ValueError"

    # вывод таблицы в консоль
    for row in t1.cells:
        for x in row:
            print(x.value, end=" ")
        print()
