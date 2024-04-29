from typing import Union


class Person:
    MAPPING = {0: "fio", 1: "job", 2: "old", 3: "salary", 4: "year_job"}

    def __init__(
        self,
        fio: str,
        job: str,
        old: int,
        salary: Union[int, float],
        year_job: int,
    ) -> None:
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job

    def __getitem__(self, index: int) -> Union[str, int, float]:
        self.validate_index(index)
        return getattr(self, self.MAPPING[index])

    def __setitem__(self, index: int, value: Union[str, int, float]) -> None:
        self.validate_index(index)
        setattr(self, self.MAPPING[index], value)

    def validate_index(self, index: int) -> bool:
        if not index <= len(self.MAPPING) - 1:
            raise IndexError("неверный индекс")
        return True

    def __next__(self):
        """Step of iterator."""
        if self.step <= len(self.MAPPING) - 1:
            result = self[self.step]
            self.step += 1
            return result
        else:
            raise StopIteration

    def __iter__(self):
        """Creation of iterator."""
        self.step = 0
        return self


if __name__ == "__main__":
    p = Person("Sereza", "Woditel", 45, 30000, 24)
    assert p[0] == "Sereza"
    assert p[4] == 24

    p[0] = "Katya"
    assert p[0] == "Katya"

    try:
        p[len(p.MAPPING)]
    except IndexError:
        assert True
    else:
        assert False

    # iter
    for i in p:
        print(i)
