from typing import Any, List, Optional, Union


class DescriptorData:
    def __set_name__(self, owner, name: str):
        self.private_name = f"_{owner.__name__}__{name}"

    def __get__(self, obj: object, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj: object, value) -> None:
        setattr(obj, self.private_name, value)


class DescriptorNext:
    def __set_name__(self, owner, name: str):
        self.private_name = f"_{owner.__name__}__{name}"

    def __get__(self, obj: object, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj: object, value) -> None:
        if self.validate(value):
            setattr(obj, self.private_name, value)
        else:
            raise ValueError

    def validate(self, value) -> bool:
        return isinstance(value, (StackObj, type(None)))


class StackObj:
    """Объект односвязного списка."""

    data = DescriptorData()
    next = DescriptorNext()

    def __init__(
        self,
        data: Any = "",
        next_: Optional["StackObj"] = None,
    ) -> None:
        self.data = data
        self.next = next_


class Stack:
    """Односвязный список."""

    top = DescriptorNext()

    def __init__(self, top: Optional["StackObj"] = None) -> None:
        self.top = top
        self.array: Union[List[StackObj], List] = []

    def push_back(self, obj: StackObj) -> None:
        """Добавление объекта класса StackObj в конец односвязного списка."""
        self.validate(obj)
        if not self.array:
            self.array.append(obj)
            self.top = obj
        else:
            self.array[-1].next = obj
            self.array.append(obj)

    def pop_back(self) -> StackObj:
        """Удаление последнего объекта из односвязного списка."""
        item = self.array.pop()
        if self.array:
            self.array[-1].next = None
        else:
            self.top = None
        return item

    def __add__(self, value: StackObj) -> "Stack":
        self.push_back(value)
        return self

    def __mul__(self, *values) -> "Stack":
        """Добавление нескольких объектов в конец односвязного списка."""
        if len(values) == 1:
            values = values[0]
        for value in values:
            if isinstance(value, str):
                value = StackObj(value)
            self.push_back(value)
        return self

    @staticmethod
    def validate(*values) -> bool:
        if all(type(i) is StackObj for i in values):
            return True
        raise ValueError


if __name__ == "__main__":
    # Объекты стека.
    obj10 = StackObj("10")
    obj9 = StackObj("9")
    obj8 = StackObj("8")
    obj7 = StackObj("7")
    obj6 = StackObj("6")
    obj5 = StackObj("5")
    obj4 = StackObj("4")
    obj3 = StackObj("3")
    obj2 = StackObj("2", obj3)
    obj1 = StackObj("1", obj2)
    assert obj1.data == "1" and obj1.next == obj2
    assert obj2.data == "2" and obj2.next == obj3
    assert obj3.data == "3" and obj3.next is None
    # Стек. Добавление первого объекта.
    stack = Stack()
    stack.push_back(obj1)
    assert stack.top == obj1
    assert stack.array == [obj1]
    # Добавление второго.
    stack.push_back(obj2)
    assert stack.top == obj1
    assert stack.array == [obj1, obj2]
    # Добавление 3 суммированием.
    stack = stack + obj3
    assert stack.top == obj1
    assert stack.array == [obj1, obj2, obj3]
    # Добавление 4 коротким суммированием.
    stack += obj4
    assert stack.array == [obj1, obj2, obj3, obj4]
    assert obj3.next == obj4
    # Умножение
    stack = stack * [obj5, obj6]
    assert stack.array == [obj1, obj2, obj3, obj4, obj5, obj6]
    stack = stack * (obj7, obj8)
    assert stack.array == [obj1, obj2, obj3, obj4, obj5, obj6, obj7, obj8]
    # Короткое умножение
    stack *= [obj9, obj10]
    assert stack.array == [
        obj1,
        obj2,
        obj3,
        obj4,
        obj5,
        obj6,
        obj7,
        obj8,
        obj9,
        obj10,
    ]
    # Умножение со строками
    stack *= ["11", "12"]
    assert stack.array[-2].data == "11"
    assert stack.array[-1].data == "12"
    # TODO: Проверка удаления
    item = stack.pop_back()
    assert item.data == "12"
    assert stack.top == obj1
    # оставим только один элемент.
    for _ in range(10):
        stack.pop_back()
    assert stack.array == [obj1]
    assert stack.top == obj1
    # Удаляем последний.
    last_item = stack.pop_back()
    assert last_item == obj1
    assert stack.top is None
    assert stack.array == []
