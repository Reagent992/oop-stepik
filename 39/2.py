from typing import List


class TriangleListIterator:
    def __init__(self, list: List[List[str]]) -> None:
        self.list = list

    def __iter__(self):
        self.__row = 0
        self.__index = 0
        self.__range = 0
        return self

    def __next__(self) -> str:
        if self.__row == len(self.list):
            raise StopIteration
        obj = self.list[self.__row][self.__index]
        self.__index += 1
        if self.__index > self.__range:
            self.__row += 1
            self.__range += 1
            self.__index = 0
        return obj


if __name__ == "__main__":
    lst = [
        ["x00"],
        ["x10", "x11"],
        ["x20", "x21", "x22"],
        ["x30", "x31", "x32", "x33"],
    ]
    it = TriangleListIterator(lst)
    lst_iter = iter(it)
    assert next(lst_iter) == "x00"
    assert next(lst_iter) == "x10"
    assert next(lst_iter) == "x11"
    for _ in lst:
        print(_)
