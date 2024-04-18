from random import randint


class Cell:

    def __init__(self) -> None:
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False

    def __bool__(self) -> bool:
        return not self.__is_open

    def __str__(self) -> str:
        if self.__is_open and self.__number:
            return str(self.__number)
        elif self.__is_open:
            return "□"
        return "■"

    @property
    def is_mine(self) -> bool:
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise ValueError("недопустимое значение атрибута")
        self.__is_mine = value

    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, value: int) -> None:
        if isinstance(value, int) and 0 <= value <= 8:
            self.__number = value
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def is_open(self) -> bool:
        return self.__is_open

    @is_open.setter
    def is_open(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise ValueError("недопустимое значение атрибута")
        self.__is_open = value


class GamePole:
    _obj = None

    def __new__(cls, *args, **kwargs):
        if cls._obj is None:
            cls._obj = super().__new__(cls)
        return cls._obj

    def __del__(self):
        GamePole._obj = None

    def __init__(self, N: int, M: int, total_mines: int) -> None:
        self._n = N
        self._m = M
        self._total_mines = total_mines
        self.__pole_cells = tuple(
            tuple(Cell() for _ in range(self._m)) for _ in range(self._n)
        )
        self.init_pole()

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        for row in self.__pole_cells:
            for x in row:
                x.is_open = False
                x.is_mine = False

        m = 0
        while m < self._total_mines:
            i = randint(0, self._n - 1)
            j = randint(0, self._m - 1)
            if self.__pole_cells[i][j].is_mine:
                continue
            self.__pole_cells[i][j].is_mine = True
            m += 1

        indx = (
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        )

        for x in range(self._n):
            for y in range(self._m):
                if not self.pole[x][y].is_mine:
                    mines = sum(
                        self.pole[x + i][y + j].is_mine
                        for i, j in indx
                        if 0 <= x + i < self._n and 0 <= y + j < self._m
                    )
                    self.pole[x][y].number = mines

    def open_cell(self, i: int, j: int) -> None:
        """Открывает ячейку по индексу."""
        if not 0 <= i < self._n and not 0 <= j < self._m:
            raise IndexError("некорректные индексы i, j клетки игрового поля")
        self.__pole_cells[i][j].__is_open = True

    def show_pole(self) -> None:
        """Отображает игровое поле в консоли."""
        for line in self.__pole_cells:
            for cell in line:
                print(cell, end="")
            print()


if __name__ == "__main__":
    # # Cell test
    # c1 = Cell()
    # assert hasattr(c1, "__is_mine")
    # assert hasattr(c1, "__number")
    # assert hasattr(c1, "__is_open")
    # try:
    #     c1.number = 9
    # except ValueError as e:
    #     assert e.args[0] == "недопустимое значение атрибута"

    # # GamePole test
    # pole1 = GamePole(10, 20, 10)
    # assert hasattr(pole1, "N")
    # assert hasattr(pole1, "M")
    # assert hasattr(pole1, "total_mines")
    # assert hasattr(pole1, "_GamePole__pole_cells")

    # pole1.init_pole()
    # pole1.show_pole()
    # pole1.open_cell(3, 2)
    # pole1.open_cell(1, 3)
    # pole1.open_cell(5, 3)
    # pole1.open_cell(7, 8)
    # pole1.open_cell(1, 8)
    # print()
    # pole1.show_pole()

    p1 = GamePole(10, 20, 10)
    p2 = GamePole(10, 20, 10)
    assert id(p1) == id(p2), "создается несколько объектов класса GamePole"
    p = p1

    cell = Cell()
    # assert (
    #     type(Cell.__is_mine) == property
    #     and type(Cell.__number) == property
    #     and type(Cell.__is_open) == property
    # ), "в классе Cell должны быть объекты-свойства is_mine, number, is_open"

    cell.__is_mine = True
    cell.__number = 5
    cell.__is_open = True
    assert bool(cell) != False, "функция bool() вернула неверное значение"

    try:
        cell.is_mine = 10
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError"

    try:
        cell.number = 10
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError"

    p.init_pole()
    m = 0
    for row in p.pole:
        for x in row:
            assert isinstance(
                x, Cell
            ), "клетками игрового поля должны быть объекты класса Cell"
            if x.is_mine:
                m += 1

    assert m == 10, "на поле расставлено неверное количество мин"
    p.open_cell(0, 1)
    p.open_cell(9, 19)

    try:
        p.open_cell(10, 20)
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось исключение IndexError"

    def count_mines(pole, i, j):
        n = 0
        for k in range(-1, 2):
            for l in range(-1, 2):
                ii, jj = k + i, l + j
                if ii < 0 or ii > 9 or jj < 0 or jj > 19:
                    continue
                if pole[ii][jj].is_mine:
                    n += 1

        return n

    for i, row in enumerate(p.pole):
        for j, x in enumerate(row):
            if not p.pole[i][j].is_mine:
                m = count_mines(p.pole, i, j)
                assert (
                    m == p.pole[i][j].number
                ), "неверно подсчитано число мин вокруг клетки"
