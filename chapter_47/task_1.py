class Person:
    __slots__ = ("_fio", "_old", "_job")

    def __init__(self, fio: str, old: int, job: str) -> None:
        self._fio = fio
        self._old = old
        self._job = job


persons = [
    Person("Суворов", 52, "полководец"),
    Person("Рахманинов", 50, "пианист, композитор"),
    Person("Балакирев", 34, "программист и преподаватель"),
    Person("Пушкин", 32, "поэт и писатель"),
]

if __name__ == "__main__":
    assert issubclass(Person, object)
    assert hasattr(Person, "__slots__")
    p = Person("vasya", 30, "enemployed")
    assert hasattr(p, "_fio")
    assert hasattr(p, "_old")
    assert hasattr(p, "_job")
