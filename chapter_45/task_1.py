from typing import List


class Student:
    def __init__(self, fio: str, group: str) -> None:
        self._fio = fio
        self._group = group
        self._lect_marks: List[int] = []  # оценки за лекции
        self._house_marks: List[int] = []  # оценки за домашние задания

    def add_lect_marks(self, mark: int) -> None:
        self._lect_marks.append(mark)

    def add_house_marks(self, mark: int) -> None:
        self._house_marks.append(mark)

    def __str__(self) -> str:
        return (
            f"Студент {self._fio}: оценки на лекциях: {str(self._lect_marks)};"
            f" оценки за д/з: {str(self._house_marks)}"
        )


class Mentor:
    def __init__(self, fio: str, subject: str) -> None:
        self._fio = fio
        self._subject = subject


# здесь продолжайте программу
class Lector(Mentor):
    def set_mark(self, student: Student, mark: int) -> None:
        student.add_lect_marks(mark)

    def __str__(self) -> str:
        return f"Лектор {self._fio}: предмет {self._subject}"


class Reviewer(Mentor):
    def set_mark(self, student: Student, mark: int) -> None:
        student.add_house_marks(mark)

    def __str__(self) -> str:
        return f"Эксперт {self._fio}: предмет {self._subject}"

if __name__ == "__main__":
    assert issubclass(Lector, Mentor)
    assert issubclass(Reviewer, Mentor)
    l = Lector("fio", "topic")
    r = Reviewer("fio", "topic")
    assert l._fio == "fio"
    assert l._subject == "topic"
    assert hasattr(l, "set_mark")
    assert hasattr(r, "set_mark")
    stud = Student("fio", "math")
    l.set_mark(stud, 5)
    assert stud._lect_marks == [5]
    r.set_mark(stud, 5)
    stud._house_marks == [5]
    assert hasattr(l, "__str__")
    assert str(l) == f"Лектор {l._fio}: предмет {l._subject}"
    assert hasattr(r, "__str__")
    assert str(r) == f"Эксперт {r._fio}: предмет {r._subject}"
