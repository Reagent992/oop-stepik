from typing import List


class FloatValue:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, float):
            raise TypeError(
                "Присваивать можно только вещественный тип данных."
            )
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Cell:
    value = FloatValue()

    def __init__(self, value: float = float()) -> None:
        self.value = value


class TableSheet:
    def __init__(self, n: int, m: int) -> None:
        self.n = n
        self.m = m
        self.cells: List[List[Cell]] = [
            [Cell() for _ in range(m)] for _ in range(n)
        ]


table = TableSheet(5, 3)
cells = table.cells
t = 1
for i in range(5):
    for f in range(3):
        cells[i][f].value += t
        t += 1

assert isinstance(table, TableSheet)
assert len(table.cells) == 5 and len(table.cells[0]) == 3

assert type(table.cells) is list

res = [int(x.value) for row in table.cells for x in row]
assert res == list(range(1, 16))

table.cells[0][0].value = 1.0
x = table.cells[1][0].value

try:
    table.cells[0][0].value = "a"
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"
