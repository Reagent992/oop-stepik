from typing import List, Optional, Union


Money = Union[int, float]


class Item:
    """Пункт расходов бюджета."""

    def __init__(self, name: str = "", money: Money = 0) -> None:
        self.validate_str(name)
        self.validate_money(money)
        self.name = name
        self.money = money

    @staticmethod
    def validate_str(value: str) -> bool:
        if isinstance(value, str):
            return True
        else:
            raise ValueError("Значение должно быть строкой.")

    @staticmethod
    def validate_money(value: Money) -> bool:
        if isinstance(value, (int, float)):
            return True
        else:
            raise ValueError("Значение должно быть int или float")

    def __add__(self, value: Union["Item", Money]) -> Money:
        if type(value) is Item:
            return self.money + value.money
        return self.money + value

    def __radd__(self, value: Union["Item", Money]) -> Money:
        return self + value


class Budget:
    """Управления семейным бюджетом."""

    def __init__(self, bought: Optional[List[Item]] = None) -> None:
        if bought:
            self.validate(bought)
            self.__bought = bought
        else:
            self.__bought = list()

    def add_item(self, item: Item) -> None:
        """Добавление статьи расхода в бюджет."""
        self.validate(item)
        self.__bought.append(item)

    def remove_item(self, index):
        """Удаление статьи расхода из бюджета по его индексу."""
        if len(self.__bought) - 1 >= index:
            self.__bought.pop(index)

    def get_items(self) -> Union[List[Item], List]:
        """Возвращает список всех статей расходов
        (список из объектов класса Item)."""
        return self.__bought

    @staticmethod
    def validate(values: Union[List[Item], Item]):
        if isinstance(values, list):
            if all(type(i) is Item for i in values):
                return True
        elif type(values) is Item:
            return True
        else:
            raise ValueError("Значение должно быть классом Item")


if __name__ == "__main__":
    itm1 = Item("Курс по Python ООП", 2000)
    itm2 = Item("Курс по Django", 5000.01)
    itm3 = Item("Курс по NumPy", 0)
    itm4 = Item("Курс по C++", 1500.10)
    assert itm1.money == 2000
    assert itm1.name == "Курс по Python ООП"
    assert itm1 + itm2 + itm3 == 7000.01

    b1 = Budget()
    assert b1.get_items() == []
    b2 = Budget([itm1, itm2])
    assert b2.get_items() == [itm1, itm2]
    b2.add_item(itm3)
    assert b2.get_items() == [itm1, itm2, itm3]
    b2.remove_item(2)
    assert b2.get_items() == [itm1, itm2]
    b2.remove_item(0)
    assert b2.get_items() == [itm2]
