from typing import Optional


def check_type(obj):
    """Проверка на принадлежность к классу ObjList."""
    if type(obj) is not ObjList:
        raise ValueError(
            f"Передан неверный тип объекта: {obj.__class__} != {ObjList}"
        )
    return True


class ObjList:
    """Объекты связанного списка."""

    __prev_obj: Optional["ObjList"] = None

    def __init__(
        self,
        data,
        next: Optional["ObjList"] = None,
    ) -> None:
        self.__prev = self.__prev_obj
        self.__data = data
        self.__next = next
        if self.__prev_obj:
            self.__prev_obj.__next = self
        self.__prev_obj = self

    def set_next(self, obj: "ObjList"):
        """Изменение приватного свойства __next на значение obj."""
        if check_type(obj):
            self.__next = obj

    def set_prev(self, obj: "ObjList"):
        """Изменение приватного свойства __prev на значение obj."""
        if check_type(obj):
            self.__prev = obj

    def set_data(self, data):
        """Изменение приватного свойства __data на значение data."""
        self.__data = data

    def get_next(self):
        """Получение значения приватного свойства __next."""
        return self.__next

    def get_prev(self):
        """Получение значения приватного свойства __prev."""
        return self.__prev

    def get_data(self):
        """Получение значения приватного свойства __data."""
        return self.__data


class LinkedList:
    """Связаный список."""

    def __init__(
        self, head: Optional[ObjList] = None, tail: Optional[ObjList] = None
    ) -> None:
        self.head = head
        self.tail = tail

    def add_obj(self, obj: ObjList):
        """Добавление нового объекта: ObjList в конец связного списка."""
        check_type(obj)
        if not self.head:
            self.head = obj
        else:
            if self.tail:
                obj.set_prev(self.tail)
                self.tail.set_next(obj)
            elif self.head:
                self.head.set_next(obj)
                obj.set_prev(self.head)
            self.tail = obj

    def remove_obj(self):
        """Удаление последнего объекта из связного списка."""
        if self.tail:
            self.tail = self.tail.get_prev()
        else:
            self.head = None

    def get_data(self):
        """Получение списка из строк локального свойства __data
        всех объектов связного списка."""
        result = []
        cur = self.head
        while cur:
            result.append(cur.get_data())
            cur = cur.get_next()
        return result


obj1 = ObjList(data="1")
obj2 = ObjList(data="2")
obj3 = ObjList(data="3")
obj4 = ObjList(data="4")
ll1 = LinkedList()
[ll1.add_obj(i) for i in (obj1, obj2, obj3, obj4)]
# print(ll1.get_data())

assert obj1.get_next() == obj2
assert obj2.get_prev() == obj1
assert obj2.get_next() == obj3

assert obj1.get_data() == "1"
assert obj2.get_data() == "2"
assert obj3.get_data() == "3"
assert obj4.get_data() == "4"


ll2 = LinkedList()
assert ll2.get_data() == list()
ll2.add_obj(obj1)
ll2.remove_obj()
assert ll2.get_data() == list()
