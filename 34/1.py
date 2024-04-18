from typing import Any, List


class NewList:
    """Список с возможностью вычитания."""

    def __init__(self, list_: List[Any] = []) -> None:
        self.__list = list_

    def __sub__(self, sub_list) -> "NewList":
        """Реализация вычитания."""
        sub_list = (
            sub_list.get_list() if type(sub_list) is NewList else sub_list
        )
        main_list = self.__list.copy()
        for item in sub_list:
            for i, value in enumerate(main_list):
                if value == item and type(value) is type(item):
                    del main_list[i]
                    break

        return NewList(main_list)

    def __rsub__(self, sub_list):
        """Реализация вычитания с неправильным порядком операндов."""
        return NewList.__sub__(NewList(sub_list), self.get_list())

    def get_list(self):
        return self.__list


if __name__ == "__main__":
    lst = NewList()
    lst1 = NewList([0, 1, -3.4, "abc", True])
    lst2 = NewList([1, 0, True])

    assert (
        lst1.get_list() == [0, 1, -3.4, "abc", True] and lst.get_list() == []
    ), "метод get_list вернул неверный список"

    res1 = lst1 - lst2
    res2 = lst1 - [0, True]
    res3 = [1, 2, 3, 4.5] - lst2
    lst1 -= lst2

    assert res1.get_list() == [
        -3.4,
        "abc",
    ], "метод get_list вернул неверный список"
    assert res2.get_list() == [
        1,
        -3.4,
        "abc",
    ], "метод get_list вернул неверный список"
    assert res3.get_list() == [
        2,
        3,
        4.5,
    ], "метод get_list вернул неверный список"
    assert lst1.get_list() == [
        -3.4,
        "abc",
    ], "метод get_list вернул неверный список"

    lst_1 = NewList([1, 0, True, False, 5.0, True, 1, True, -7.87])
    lst_2 = NewList([10, True, False, True, 1, 7.87])
    res = lst_1 - lst_2
    assert res.get_list() == [
        0,
        5.0,
        1,
        True,
        -7.87,
    ], "метод get_list вернул неверный список"

    a = NewList([2, 3])
    res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]
    assert res_4.get_list() == [1, 2], "метод get_list вернул неверный список"
