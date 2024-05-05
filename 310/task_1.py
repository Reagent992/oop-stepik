from random import randint
from typing import Iterator, List, Tuple, Type


class CellDescriptor:
    def __set_name__(self, owner: Type[object], name: str):
        self.private_name = f"_{owner.__name__}__{name}"

    def __get__(self, obj: object, objtype=None):
        return getattr(obj, self.private_name, None)

    def __set__(self, obj: object, value) -> None:
        if not isinstance(value, int):
            raise TypeError("Wrong type passed")
        if not 0 <= value <= 2:
            raise ValueError("Wrong value passed")
        setattr(obj, self.private_name, value)


class Cell:
    value = CellDescriptor()
    emoji_dict = {0: "\u2b1c", 1: "\u274c", 2: "\u2b55"}

    def __init__(self, value: int = 0) -> None:
        """0 - клетка свободна; 1 - стоит крестик; 2 - стоит нолик."""
        self.value = value

    def wipe(self) -> None:
        """Set value to 0."""
        self.value = 0

    def __bool__(self) -> bool:
        return not bool(self.value)

    def __str__(self):
        return self.emoji_dict[self.value]


class TicTacToe:
    field_size = 3
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)
    WIN_COMBINATIONS = (
        # Rows
        ((0, 0), (0, 1), (0, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),
        # Columns
        ((0, 0), (1, 0), (2, 0)),
        ((0, 1), (1, 1), (2, 1)),
        ((0, 2), (1, 2), (2, 2)),
        # Diagonals
        ((0, 0), (1, 1), (2, 2)),
        ((0, 2), (1, 1), (2, 0)),
    )

    def __init__(self) -> None:
        self.pole = [
            [Cell() for _ in range(self.field_size)]
            for _ in range(self.field_size)
        ]
        self.__human_cells: List[Tuple[int, int]] = []
        self.__computer_cells: List[Tuple[int, int]] = []

    def __getitem__(self, index: Tuple[int, int]) -> int:
        self.validate_index(index)
        row, col = index
        return self.pole[row][col].value

    def __setitem__(self, index: Tuple[int, int], value: int) -> None:
        self.validate_index(index)
        row, col = index
        self.pole[row][col].value = value
        self.__coordinate_lists_of_cells(index, value)

    def __coordinate_lists_of_cells(
        self, index: Tuple[int, int], value: int
    ) -> None:
        if value == TicTacToe.HUMAN_X:
            self.__human_cells.append(index)
        elif value == TicTacToe.COMPUTER_O:
            self.__computer_cells.append(index)
        elif value == TicTacToe.FREE_CELL:
            if index in self.__computer_cells:
                del self.__computer_cells[self.__computer_cells.index(index)]
            if index in self.__human_cells:
                del self.__human_cells[self.__human_cells.index(index)]

    def validate_index(self, index: Tuple[int, int]) -> bool:
        if (
            len(index) != 2
            or not isinstance(index, tuple)
            or not isinstance(index[0], int)
            or not isinstance(index[1], int)
            or not 0 <= index[0] <= 2
            or not 0 <= index[1] <= 2
        ):
            raise IndexError("некорректно указанные индексы")
        return True

    def __iter__(self) -> Iterator[List[Cell]]:
        for row in self.pole:
            yield row

    def init(self) -> None:
        """Clear game-field."""
        self.__human_cells = []
        self.__computer_cells = []
        for row in self:
            for cell_obj in row:
                cell_obj.wipe()

    def show(self) -> None:
        """Print game-field."""
        for row in self:
            print(" ".join([str(i) for i in row]))

    def human_go(self) -> None:
        index = input()
        row, col = map(int, index.split())
        self.validate_index((row, col))
        self[row, col] = self.HUMAN_X

    def computer_go(self) -> None:
        choosing_field = True
        while choosing_field:
            row, col = randint(0, 2), randint(0, 2)
            rand_field = self.pole[row][col]
            if rand_field:
                rand_field.value = self.COMPUTER_O
                choosing_field = False
            elif not self.__empty_field_exist():
                choosing_field = False
                break

    def __empty_field_exist(self) -> bool:
        return self.field_size * self.field_size > (
            len(self.__computer_cells) + len(self.__human_cells)
        )

    def check_win(self, fields: List[Tuple[int, int]]) -> bool:
        for win_combination in self.WIN_COMBINATIONS:
            if all(combination in fields for combination in win_combination):
                return True
        return False

    @property
    def is_human_win(self) -> bool:
        return self.check_win(self.__human_cells)

    @property
    def is_computer_win(self) -> bool:
        return self.check_win(self.__computer_cells)

    @property
    def is_draw(self) -> bool:
        return (
            self.is_human_win is False and self.is_computer_win is False
        ) and not self.__empty_field_exist()

    def play(self) -> None:
        # FIXME: infinite loop when computer win or draw.
        computer_win = False
        human_win = False
        draw = False
        while not any((computer_win, human_win, draw)):
            self.show()
            self.human_go()
            self.computer_go()
            computer_win = self.is_computer_win
            human_win = self.is_human_win
            draw = self.is_draw
        if human_win:
            print("Congratulations! You are Win!")
        elif computer_win:
            print("You loose. Better luck next time!")
        elif draw:
            print("Draw!")
        self.init()


if __name__ == "__main__":
    ttt = TicTacToe()
    ttt.play()
