from typing import Any, Tuple


class Cell:
    def __init__(self, data: Any = 0) -> None:
        self.__data = data

    @property
    def data(self) -> Any:
        return self.__data

    @data.setter
    def data(self, value: Any) -> None:
        self.__data = value

    @data.deleter
    def data(self) -> None:
        del self.__data


class TableValues:
    def __init__(
        self, rows: int = 0, cols: int = 0, type_data: Any = int
    ) -> None:
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self._table = [[Cell() for _ in range(cols)] for _ in range(rows)]

    def __getitem__(self, index: Tuple[int, int]) -> Any:
        row, col = self.validate_index(index)
        return self._table[row][col].data

    def __setitem__(self, index: Tuple[int, int], value: Any) -> None:
        row, col = self.validate_index(index)
        if not isinstance(value, self.type_data):
            raise TypeError("неверный тип присваиваемых данных")
        self._table[row][col].data = value

    def validate_index(self, index: Tuple[int, int]) -> Tuple[int, int]:
        if not isinstance(index, tuple) or len(index) != 2:
            raise ValueError
        row, col = index
        if not 0 <= row <= self.rows - 1 and not 0 <= col <= self.cols - 1:
            raise IndexError("неверный индекс")
        return row, col

    def __iter__(self):
        for row in self._table:
            yield [i.data for i in row]


if __name__ == "__main__":
    # Cell
    c1 = Cell(123)
    assert c1.data == 123
    c1.data = 321
    assert c1.data == 321
    del c1.data
    assert not hasattr(c1, "_Cell__data")
    c1.data = 543
    assert c1.data == 543

    # TableValues
    tv = TableValues(3, 3, int)
    assert tv.rows == 3
    assert tv.cols == 3
    assert tv.type_data == int
    assert isinstance(tv._table[0][0], Cell)
    tv[0, 0] = 10
    assert tv[0, 0] == 10

    for row in tv:  # перебор по строкам
        for value in row:  # перебор по столбцам
            print(value, end=" ")  # вывод значений ячеек в консоль
        print()
