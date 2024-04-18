import sys
from typing import Dict, List, Optional


class DataBase:
    def __init__(self, path: str) -> None:
        self.path = path
        self.dict_db: Dict["Record", List["Record"]] = dict()

    def write(self, record: "Record") -> None:
        if record in self.dict_db:
            self.dict_db[record].append(record)
        else:
            self.dict_db[record] = [record]

    def read(self, pk: int) -> Optional["Record"]:
        for i in self.dict_db:
            if i.pk == pk:
                return i
        return None


class Record:
    """Запись в БД."""

    PK = 1

    def __init__(self, fio: str, descr: str, old: int) -> None:
        self.fio = fio
        self.descr = descr
        self.old = old
        self.pk = Record.PK
        Record.PK += 1

    def __hash__(self) -> int:
        return hash((self.fio.lower(), self.old))

    def __eq__(self, obj: "Record") -> bool:  # type: ignore
        return hash(self) == hash(obj)


db = DataBase("./file.name")

TEST = False
if TEST:
    lst_in = """Балакирев С.М.; программист; 33
Кузнецов Н.И.; разведчик-нелегал; 35
Суворов А.В.; полководец; 42
Иванов И.И.; фигурант всех подобных списков; 26
Балакирев С.М.; преподаватель; 33""".split("\n")
else:
    lst_in = list(map(str.strip, sys.stdin.readlines()))

for line in lst_in:
    name, desc, age = line.split("; ")
    db.write(Record(name, desc, int(age)))

if __name__ == "__main__":
    # Record check
    r1 = Record("Vasya", "Good boy", 18)
    r2 = Record("Vasya", "Good boy", 18)
    r3 = Record("Lena", "good girl", 20)
    assert r1 == r2
    assert r1 != r3
    # DataBase check
    d1 = DataBase("C:/")
    assert hasattr(d1, "dict_db")
