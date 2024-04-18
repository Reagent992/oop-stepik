from typing import List, Optional


class StackObj:
    """Объект односвязного списка."""

    _prev_obj: Optional["StackObj"] = None

    def __init__(self, data: str, next: Optional["StackObj"] = None) -> None:
        self.__data = data
        self.__next = next
        if self._prev_obj:
            self._prev_obj.__next = self
        else:
            self._prev_obj = self

    @staticmethod
    def check_type(value: Optional["StackObj"]) -> bool:
        return type(value) in (StackObj, None)

    @property
    def next(self) -> Optional["StackObj"]:
        return self.__next

    @next.setter
    def next(self, value: Optional["StackObj"]) -> None:
        if self.check_type(value):
            self.__next = value

    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, value: str) -> None:
        if isinstance(value, str):
            self.__data = value


class Stack:
    """Управление односвязным списком."""

    def __init__(
        self,
        top: Optional["StackObj"] = None,
        tail: Optional["StackObj"] = None,
    ) -> None:
        self.top = top
        self.tail = tail
        self._obj_list: List[StackObj] = []
        if self.top:
            self.obj_list_append(self.top)
        if self.tail and self.top:
            self.top.next = self.tail
            self.obj_list_append(self.tail)

    def push(self, obj: StackObj):
        """Добавление объекта в конец списка."""
        if self.tail:
            self.tail.next = obj
            self.tail = obj
            self.obj_list_append(self.tail)
        else:
            self.top = obj
            self.tail = obj
            self.obj_list_append(obj)

    def pop(self) -> Optional["StackObj"]:
        """Извлечение последнего объекта с его удалением."""
        cur = self.tail
        if len(self._obj_list) > 1:
            self._obj_list.pop()
            self.tail = self._obj_list[-1]
            self.tail.next = None
        elif len(self._obj_list) == 1:
            self._obj_list.pop()
            self.tail = self.top = None
        return cur

    def get_data(self) -> list:
        result: List[str] = []
        if self.tail:
            for i in self._obj_list:
                result.append(i.data)
        return result

    def obj_list_append(self, value: StackObj) -> None:
        self._obj_list.append(value)


# # Stack
# obj1 = StackObj("1")
# obj2 = StackObj("2")
# obj3 = StackObj("3")
# obj4 = StackObj("4")
# obj5 = StackObj("5")
# st = Stack(obj1)
# st.push(obj2)
# st.push(obj3)
# assert obj2.next == obj3
# st.push(obj4)
# st.push(obj5)
# print(st.get_data())
# assert st.pop() == obj5
# print(st.get_data())
# assert st.pop() == obj4
# assert st.pop() == obj3
# assert st.pop() == obj2
# assert st.pop() == obj1
# print(st.get_data())
# # ----
# st.push(obj1)
# st.push(obj2)
# st.pop()
# st.push(obj3)
# assert st.get_data() == ["1", "3"]
# # --
# st2 = Stack()
# assert st2.top is None
# st2.push(obj1)
# assert st2.top == obj1
# # StackObj
# obj2.data = "10"
# assert obj2.data == "10"

s = Stack()
top = StackObj("obj_1")
s.push(top)
s.push(StackObj("obj_2"))
s.push(StackObj("obj_3"))
s.pop()

res = s.get_data()
assert res == [
    "obj_1",
    "obj_2",
], f"метод get_data вернул неверные данные: {res}"
assert (
    s.top == top
), "атрибут top объекта класса Stack содержит неверное значение"

h = s.top
while h:
    res = h.data
    h = h.next

s = Stack()
top = StackObj("obj_1")
s.push(top)
s.pop()
assert (
    s.get_data() == []
), f"метод get_data вернул неверные данные: {s.get_data()}"

n = 0
h = s.top
while h:
    h = h.next
    n += 1

assert (
    n == 0
), "при удалении всех объектов, стек-подобная стурктура оказалась не пустой"

s = Stack()
top = StackObj("name_1")
s.push(top)
obj = s.pop()
assert obj == top, "метод pop() должен возвращать удаляемый объект"
