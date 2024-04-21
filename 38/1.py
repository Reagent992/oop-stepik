from typing import Any


class Record:
    def __init__(self, **kwargs) -> None:
        self.__dict__ = kwargs

    def __getitem__(self, item: int) -> Any:
        if self.validation_by_index(item):
            return list(self.__dict__.values())[item]

    def __setitem__(self, key, value) -> None:
        if isinstance(key, str) and hasattr(self, key):
            self.key = value
        elif self.validation_by_index(key):
            setattr(self, list(self.__dict__.keys())[key], value)

    def validation_by_index(self, index: int) -> bool:
        if isinstance(index, int) and index <= len(self.__dict__) - 1:
            return True
        else:
            raise IndexError("неверный индекс поля")


if __name__ == "__main__":
    r = Record(pk=1, title="Python ООП", author="Балакирев")
    assert (
        hasattr(r, "pk") and hasattr(r, "title") and hasattr(r, "author")
    ), "В объекте класса не созданы переданные аттрибуты"
    assert (
        r.pk == 1 and r.title == "Python ООП" and r.author == "Балакирев"
    ), "Неверные значения в объекте класса"
    assert (
        r[0] == 1 and r[1] == "Python ООП" and r[2] == "Балакирев"
    ), "Неверные ключи при доступе по индексу"
    r.pk = 10
    assert r.pk == 10, "Неверно работает изменение аттрибута по индексу"
    assert r[0] == 10
    r[0] = 11
    assert r.pk == 11

    try:
        r[3]
    except IndexError:
        assert True
    else:
        assert False, (
            "Исключение IndexError не поднимается при"
            " обращение к несуществующему индексу"
        )
