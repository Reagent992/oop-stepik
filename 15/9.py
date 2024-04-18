import random
from typing import List


class Cell:
    """Представления клетки игрового поля."""

    def __init__(
        self, around_mines: int = 0, mine: bool = False, fl_open: bool = False
    ) -> None:
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = fl_open


class GamePole:
    """Управление игровым полем, размером N x N клеток."""

    def __init__(self, n: int, m: int) -> None:
        self.n = n
        self.m = m
        self.pole = self.init(n, m)

    def init(self, n, m):
        """Расставляем мины по полю."""
        game_field = [[Cell(0, False) for _ in range(n)] for _ in range(n)]
        for _ in range(m):
            game_field_len = len(game_field)
            mine_line_index = random.randint(0, game_field_len - 1)
            mine_line = game_field[mine_line_index]
            mine_line_len = len(mine_line)
            mine_field_index = random.randint(0, mine_line_len - 1)
            field = mine_line[mine_field_index]
            # Проверка что в поле уже не стоит мина
            if field.mine:
                swap = False
                while swap is not True:
                    mine_field_index = random.randint(0, mine_line_len - 1)
                    field = mine_line[mine_field_index]
                    if not field.mine:
                        swap = True

            field.mine = True
            self.around_mines(
                game_field_len,
                game_field,
                mine_line_index,
                mine_field_index,
                mine_line,
                mine_line_len,
            )
        return game_field

    def choose_mine_field(self):
        return True

    def around_mines(
        self,
        game_field_len: int,
        game_field: List[List[Cell]],
        mine_line_index: int,
        mine_field_index: int,
        mine_line: List[Cell],
        mine_line_len: int,
    ):
        """Расставляем around_mines."""
        # Горизонтальные around_mines:
        if mine_field_index != 0:
            left_field = mine_line[mine_field_index - 1]
            left_field.around_mines += 1
        if mine_field_index < mine_line_len - 1:
            right_field = mine_line[mine_field_index + 1]
            right_field.around_mines += 1
        # Вертикальные, верхние around_mines.
        if mine_line_index != 0:
            prev_line = game_field[mine_line_index - 1]
            top_center_field = prev_line[mine_field_index]
            top_center_field.around_mines += 1

            if mine_field_index != 0:
                top_left_field = prev_line[mine_field_index - 1]
                top_left_field.around_mines += 1

            if mine_field_index < mine_line_len - 1:
                top_right_field = prev_line[mine_field_index + 1]
                top_right_field.around_mines += 1
        # Вертикальные, нижние around_mines.
        if mine_line_index < game_field_len - 1:
            next_line = game_field[mine_line_index + 1]
            bottom_center_field = next_line[mine_field_index]
            bottom_center_field.around_mines += 1

            if mine_field_index != 0:
                bottom_left_field = next_line[mine_field_index - 1]
                bottom_left_field.around_mines += 1

            if mine_field_index < mine_line_len - 1:
                bottom_right_field = next_line[mine_field_index + 1]
                bottom_right_field.around_mines += 1

    def show(self):
        """Отображение поля в консоли."""
        field = []
        for line in self.pole:
            # field.append(" ".join(["*" if i.fl_open else "#" for i in line]))
            field.append(
                " ".join(
                    ["*" if i.mine else str(i.around_mines) for i in line]
                )
            )
        return "\n".join(field)


pole_game = GamePole(10, 12)
print(pole_game.show())
