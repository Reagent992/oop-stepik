from typing import List

class IterColumn:
    def __init__(self, lst: List[List[str]], column: int) -> None:
        self.lst = lst
        self.column = column

    def __next__(self):
        if self.index <= len(self.lst) - 1:
            obj = self.lst[self.index][self.column]
            self.index += 1
            return obj
        else:
            raise StopIteration

    def __iter__(self):
        self.index = 0
        return self

if __name__ == "__main__":
    lst = [["x11", "x12", "x13", "x14"],
           ["x21", "x22", "x23", "x24"]]
    it = IterColumn(lst, 2)
    assert it.lst == lst
    for _ in it:
        print(_)
