from abc import ABC
import time
from typing import Any, Dict, Union

filters_type = Union["Mechanical", "Aragon", "Calcium"]


class Filter(ABC):
    def __init__(self, date: float) -> None:
        self.date = date

    def __setattr__(self, name: str, value: Any) -> None:
        if name not in self.__dict__:
            return super().__setattr__(name, value)


class Mechanical(Filter):
    pass


class Aragon(Filter):
    pass


class Calcium(Filter):
    pass


class GeyserClassic:
    MAX_DATE_FILTER = 100
    type_check = {"1": Mechanical, "2": Aragon, "3": Calcium}

    def __init__(self) -> None:
        self.filters: Dict[str, filters_type] = dict()

    def add_filter(self, slot_num: int, filter: filters_type) -> None:
        if self.type_check[str(slot_num)] == type(filter):
            self.filters.setdefault(str(slot_num), filter)

    def remove_filter(self, slot_num: int) -> None:
        self.filters.pop(str(slot_num))

    def get_filters(self):
        return self.filters.values()

    def water_on(self):
        fl = self.filters.values()
        if len(self.filters) == 3 and None not in fl:
            return all(
                [0 <= time.time() - i.date <= self.MAX_DATE_FILTER for i in fl]
            )
        return False


# if __name__ == "__main__":
#     m1 = Mechanical(2022)
#     m2 = Mechanical(2023)
#     a1 = Aragon(2000)
#     assert m1.date == 2022
#     m1.date = 2000
#     assert m1.date == 2022
#     g = GeyserClassic()
#     g.add_filter(1, m1)
#     g.add_filter(1, m2)
#     f = g.filters.get("1")
#     assert f == m1
#     g.add_filter(1, a1)
#     assert f == m1
#     # remove
#     g.remove_filter(1)
#     assert g.filters.get("1") is None
#     g.add_filter(1, m1)
#     g.add_filter(1, m2)
#     f = g.filters.get("1")
#     assert f == m1
#     # get filters
#     g.add_filter(2, a1)
#     print(g.get_filters())


my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))

assert (
    my_water.water_on() == False
), "метод water_on вернул True, хотя не все фильтры были установлены"

my_water.add_filter(3, Calcium(time.time()))
assert (
    my_water.water_on()
), "метод water_on вернул False при всех трех установленных фильтрах"

f1, f2, f3 = my_water.get_filters()
assert (
    isinstance(f1, Mechanical)
    and isinstance(f2, Aragon)
    and isinstance(f3, Calcium)
), "фильтры должны быть устанлены в порядке: Mechanical, Aragon, Calcium"

my_water.remove_filter(1)
assert (
    my_water.water_on() == False
), "метод water_on вернул True, хотя один из фильтров был удален"

my_water.add_filter(1, Mechanical(time.time()))
assert (
    my_water.water_on()
), "метод water_on вернул False, хотя все три фильтра установлены"

f1, f2, f3 = my_water.get_filters()
my_water.remove_filter(1)

my_water.add_filter(
    1, Mechanical(time.time() - GeyserClassic.MAX_DATE_FILTER - 1)
)
assert (
    my_water.water_on() == False
), "метод water_on вернул True, хотя у одного фильтра истек срок его работы"

f1 = Mechanical(1.0)
f2 = Aragon(2.0)
f3 = Calcium(3.0)
assert (
    0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1
), "неверное значение атрибута date в объектах фильтров"

f1.date = 5.0
f2.date = 5.0
f3.date = 5.0

assert (
    0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1
), "локальный атрибут date в объектах фильтров должен быть защищен от изменения"
