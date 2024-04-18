from typing import List, Union


class NameDescriptor:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if self.validate(value):
            setattr(obj, self.private_name, value)

    def validate(self, value):
        return isinstance(value, str)


class WeightDescriptor:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if self.validate(value):
            setattr(obj, self.private_name, value)

    def validate(self, value):
        return isinstance(value, (int, float))


class Thing:
    name = NameDescriptor()
    weight = WeightDescriptor()

    def __init__(self, name: str, weight: Union[int, float]) -> None:
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self, max_weight: int) -> None:
        self.max_weight = max_weight
        self.__things: List[Thing] = list()

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing):
        """Добавление нового предмета в рюкзак."""
        if (
            type(thing) is Thing
            and 0 <= self.get_total_weight() + thing.weight <= self.max_weight
        ):
            self.__things.append(thing)

    def remove_thing(self, indx):
        """Удаление предмета по индексу."""
        del self.__things[indx]

    def get_total_weight(self) -> int:
        """Возвращает суммарный вес предметов в рюкзаке."""
        return sum([i.weight for i in self.__things])


if __name__ == "__main__":
    # Thing test
    t1 = Thing("Ручка", 0.01)
    t2 = Thing("Пенал", 1.36)
    t3 = Thing("Штанга", 60)
    assert t1.name == "Ручка"
    assert t1.weight == 0.01
    t1.name = 1
    assert t1.name == "Ручка"
    t1.weight = "Вес"
    assert t1.weight == 0.01
    # Bag test
    bag1 = Bag(max_weight=35)
    assert bag1.max_weight == 35
    [bag1.add_thing(i) for i in (t1, t2, t3)]
    assert bag1.get_total_weight() == 1.37
    assert bag1.things == [t1, t2]
    try:
        bag1.things = []  # type: ignore
    except AttributeError:
        True
    bag1.remove_thing(0)
    assert bag1.things == [t2]
    assert bag1.get_total_weight() == 1.36
