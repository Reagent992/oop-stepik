from typing import Optional


class Descriptor:
    def __set_name__(self, owner, name):
        self.private_name = f"_{owner.__name__}__{name}"

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        setattr(obj, self.private_name, value)


class ObjList:
    """Объект связанного списка."""

    data = Descriptor()
    prev = Descriptor()
    next = Descriptor()

    def __init__(self, data=None) -> None:
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    """Связанный список."""

    def __init__(
        self,
        head: Optional[ObjList] = None,
        tail: Optional[ObjList] = None,
    ) -> None:
        self.head = head
        self.tail = tail

    def add_obj(self, obj: ObjList) -> None:
        """Добавление нового объекта в конец связанного списка."""
        if isinstance(obj, ObjList):
            if not self.head:
                self.head = obj
            elif not self.tail:
                self.tail = obj
                obj.prev = self.head
                self.head.next = obj
            else:
                self.tail.next = obj
                obj.prev = self.tail
                self.tail = obj

    def remove_obj(self, index_: int) -> None:
        """Удаление объекта списка по индексу."""
        current_obj = self.get_obj_by_index(index_)

        if current_obj:
            if current_obj.prev:
                prev = current_obj.prev
                if current_obj.next:
                    prev.next = current_obj.next
                else:
                    prev.next = None
                    self.tail = prev
            else:
                self.head = None
                self.tail = None
        else:
            self.head = None
            self.tail = None

    def __call__(self, index_: int):
        """Вывод значения объекта связанного списка по индексу."""
        current_obj = self.get_obj_by_index(index_)
        if current_obj:
            return current_obj.data
        else:
            return None

    def __len__(self) -> int:
        """Длина связанного списка."""
        result = 0
        if self.head:
            result = 1
            current_obj: Optional[ObjList] = self.head
            while getattr(current_obj, "next", None):
                result += 1
                current_obj = getattr(current_obj, "next", None)

        return result

    def get_obj_by_index(self, index_: int) -> Optional[ObjList]:
        """Получение объекта связанного списка по индексу."""
        current_obj: Optional[ObjList] = None
        for _ in range(index_ + 1):
            if current_obj:
                current_obj = current_obj.next
            else:
                current_obj = self.head
        return current_obj


if __name__ == "__main__":
    # Проверка объектов списка.
    obj1 = ObjList(1)
    obj2 = ObjList(2)
    obj3 = ObjList(3)
    obj4 = ObjList(4)
    assert obj1.data == 1
    assert obj2.data == 2
    assert obj3.data == 3

    # Проверка связанного списка.
    linked_list = LinkedList()
    linked_list.add_obj(obj1)
    linked_list.add_obj(obj2)
    linked_list.add_obj(obj3)
    linked_list.add_obj(obj4)
    assert linked_list.head == obj1
    assert linked_list.tail == obj4
    linked_list.remove_obj(2)
    assert linked_list.tail == obj4
    assert len(linked_list) == 3
    assert linked_list(2) == 4

    # с задания:
    linked_lst = LinkedList()
    linked_lst.add_obj(ObjList("Sergey"))
    linked_lst.add_obj(ObjList("Balakirev"))
    linked_lst.add_obj(ObjList("Python"))
    linked_lst.remove_obj(2)
    linked_lst.add_obj(ObjList("Python ООП"))
    assert len(linked_lst) == 3
    assert linked_lst(1) == "Balakirev"

    # Удаление единственного объекта.
    list2 = LinkedList()
    list2.add_obj(ObjList("data"))
    list2.remove_obj(0)
    assert len(list2) == 0
    assert list2.head is None
    assert list2.tail is None

    # Удаление из пустого списка.
    list22 = LinkedList()
    list22.remove_obj(0)
    assert len(list22) == 0
    assert list2.head is None
    assert list2.tail is None

    # Удаление второго объекта списка.
    list3 = LinkedList()
    obj10 = ObjList(1)
    obj20 = ObjList(2)
    list3.add_obj(obj10)
    list3.add_obj(obj20)
    list3.remove_obj(1)
    assert len(list3) == 1
    assert list3.head == obj10
    assert list3.tail == obj10
