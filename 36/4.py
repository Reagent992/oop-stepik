import sys


class BookStudy:
    def __init__(self, name: str, author: str, year: int) -> None:
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self) -> int:
        return hash((self.name.lower(), self.author.lower()))


TEST = False
if TEST:
    lst_in = """Python; Балакирев С.М.; 2020
Python ООП; Балакирев С.М.; 2021
Python ООП; Балакирев С.М.; 2022
Python; Балакирев С.М.; 2021""".split(
        "\n"
    )
else:
    lst_in = list(map(str.strip, sys.stdin.readlines()))

lst_bs = []
for line in lst_in:
    name, desc, age = line.split("; ")
    lst_bs.append(BookStudy(name, desc, int(age)))

hashes = []
unique_books = 0
for book in lst_bs:
    if hash(book) in hashes:
        continue
    else:
        hashes.append(hash(book))
        unique_books += 1

if __name__ == "__main__":
    # BookStudy Class tests
    bs1 = BookStudy("Python", "Miron", 1999)
    assert hasattr(bs1, "name")
    assert hasattr(bs1, "author")
    assert hasattr(bs1, "year")
    assert bs1.name == "Python" and bs1.author == "Miron" and bs1.year == 1999
    # hash
    bs2 = BookStudy("Python", "Miron", 1999)
    assert hash(bs1) == hash(bs2)
    # ub
    assert unique_books == 2
