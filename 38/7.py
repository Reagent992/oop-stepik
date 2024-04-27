from typing import Tuple, Union

TTT_INDEX = Union[Tuple[int, int], slice, Tuple[int, slice]]


class Cell:
    def __init__(self) -> None:
        """is_free - True, если клетка свободна; False в противном случае;
        value - значение поля: 1 - крестик; 2 - нолик (по умолчанию 0)."""
        self.is_free = True
        self._value = 0

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, new_value: int) -> None:
        if isinstance(new_value, int):  # and 0 <= new_value <= 2:
            if self.is_free is False:
                raise ValueError("клетка уже занята")
            self._value = new_value
        else:
            raise ValueError("Wrong value passed")

    def __bool__(self) -> bool:
        return bool(self.is_free)


class TicTacToe:
    def __init__(self) -> None:
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    def clear(self) -> None:
        """Clear game field."""
        for row in self.pole:
            for obj in row:
                obj.is_free = True
                obj.value = 0

    def __getitem__(self, index):
        if isinstance(index, tuple):
            if all(isinstance(i, int) for i in index):
                # default index work like obj[1:2:3]
                self.validate_tuple_index(index)
                row, cell = index
                return self.pole[row][cell].value
            elif all(isinstance(i, (slice, int)) for i in index):
                # Some bullshit-slice
                # 1. get variables from tuple
                # 2. validate
                # 3. return
                # TODO: Разделение на столбец и строку
                if isinstance(index[0], slice):
                    index_slice, column_index = index
                    self.validate_index(column_index)
                    return tuple(row[column_index].value for row in self.pole)
                elif isinstance(index[1], slice):
                    row_index, index_slice = index
                    self.validate_index(row_index)
                    return tuple(i.value for i in self.pole[row_index])
                # TODO: should i use slice here?
            raise NotImplementedError
        elif isinstance(index, slice) and self.validate_slice(index):
            # default slice
            self.validate_slice(index)
            raise NotImplementedError
        raise NotImplementedError

    def __setitem__(self, index: Tuple[int, int], value: int) -> None:
        if (
            isinstance(index, tuple)
            and len(index) == 2
            and all(isinstance(i, int) for i in index)
            and self.validate_tuple_index(index)
        ):
            # set by TicTacToe[0, 2] = 2
            row, obj_index = index
            self.pole[row][obj_index].value = value
        else:
            raise NotImplementedError

    def validate_index(self, index: int) -> bool:
        if not -3 <= index <= 2:
            raise IndexError("неверный индекс клетки")
        return True

    def validate_tuple_index(self, index: Tuple[int, int]) -> bool:
        if not all(-3 <= i <= 2 for i in index) or len(index) != 2:
            raise IndexError("неверный индекс клетки")
        return True

    def validate_slice(self, user_slice: slice) -> bool:
        if not isinstance(user_slice, slice):
            raise ValueError
        if not all(-3 <= i <= 2 for i in (user_slice.start, user_slice.stop)):
            raise IndexError("неверный индекс клетки")
        return True


if __name__ == "__main__":
    # Cell
    c1 = Cell()
    c2 = Cell()
    c2.value = 1
    c2.is_free = False
    assert c1.is_free is True and c1.value == 0
    assert c2.is_free is False and c2.value == 1
    assert bool(c1) and not bool(c2)

    try:
        c2.value = 10
    except ValueError:
        assert True
    else:
        assert False, "Cell should be open and value should be between 0 and 2"

    # TicTacToe
    t1 = TicTacToe()
    for row in t1.pole:
        for obj in row:
            assert (
                isinstance(obj, Cell)
                and obj.is_free is True
                and obj.value == 0
            )

    # TicTacToe get by index
    assert isinstance(t1[0, 0], int)
    try:
        t1[-3, 3]
    except IndexError:
        assert True
    else:
        assert False

    # TicTacToe by slice
    # assert len(t1[0:1]) == 2

    # TicTacToe set Cell value by index
    t1[2, 0] = 1
    t1[2, 1] = 1
    t1[2, 2] = 1
    assert t1[2, 0] == 1
    assert t1[2, 1] == 1
    assert t1[2, 2] == 1

    # get by crazy (index, slice)
    # it's a tuple(slice, int) or tuple(int, slice)
    # TODO: test row and column
    assert t1[:, 2]
