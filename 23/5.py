from typing import List


class TVProgram:
    def __init__(self, name: str) -> None:
        self.name = name
        self.items: List["Telecast"] = list()

    def add_telecast(self, tl: "Telecast"):
        """добавление новой телепередачи в список items;"""
        if type(tl) is Telecast:
            self.items.append(tl)

    def remove_telecast(self, indx: int):
        """удаление телепередачи по ее порядковому номеру"""
        if isinstance(indx, int):
            for i in self.items:
                if i.uid == indx:
                    self.items.remove(i)
                    break


class Telecast:
    def __init__(self, id: int, name: str, duration: int) -> None:
        self.__id = id
        self.__name = name
        self.__duration = duration

    @property
    def uid(self):
        return self.__id

    @uid.setter
    def uid(self, value: int):
        if isinstance(value, int):
            self.__id == value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if isinstance(value, str):
            self.__name = value

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value: int):
        if isinstance(value, int):
            self.__duration = value


assert hasattr(TVProgram, "add_telecast") and hasattr(
    TVProgram, "remove_telecast"
), "в классе TVProgram должны быть методы add_telecast и remove_telecast"

pr = TVProgram("Первый канал")
pr.add_telecast(Telecast(1, "Доброе утро", 10000))
pr.add_telecast(Telecast(3, "Новости", 2000))
t = Telecast(2, "Интервью с Балакиревым", 20)
pr.add_telecast(t)

pr.remove_telecast(3)
assert (
    len(pr.items) == 2
), "неверное число телеперач, возможно, некорректно работает метод remove_telecast"
assert (
    pr.items[-1] == t
), "удалена неверная телепередача (возможно, вы удаляете не по __id, а по порядковому индексу в списке items)"

assert (
    type(Telecast.uid) == property
    and type(Telecast.name) == property
    and type(Telecast.duration) == property
), "в классе Telecast должны быть объекты-свойства uid, name и duration"

for x in pr.items:
    assert hasattr(x, "uid") and hasattr(x, "name") and hasattr(x, "duration")

assert (
    pr.items[0].name == "Доброе утро"
), "объект-свойство name вернуло неверное значение"
assert (
    pr.items[0].duration == 10000
), "объект-свойство duration вернуло неверное значение"

t = Telecast(1, "Доброе утро", 10000)
t.uid = 2
t.name = "hello"
t.duration = 10
