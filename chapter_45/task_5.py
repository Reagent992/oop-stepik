from abc import ABC, abstractmethod
from typing import Any, Callable, Optional


class StackObj:
    def __init__(self, data: str, next: Optional["StackObj"] = None) -> None:
        self._data = data
        self._next = next


class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        pass

    @abstractmethod
    def pop_back(self):
        pass


def validate_stack_obj(func: Callable) -> Callable:
    def wrapper(link: "Stack", obj: StackObj) -> Any:
        if not isinstance(obj, StackObj):
            raise TypeError
        return func(link, obj)

    return wrapper


class Stack(StackInterface):
    def __init__(self, top=None) -> None:
        self._top = top

    @validate_stack_obj
    def push_back(self, obj: StackObj) -> None:
        if self._top is None:
            self._top = obj
        else:
            obj._next = self._top
            self._top = obj

    def pop_back(self) -> StackObj:
        result = self._top
        if self._top._next is not None:
            self._top = self._top._next
        else:
            self._top = None
        return result


if __name__ == "__main__":
    assert issubclass(StackInterface, ABC)
    assert hasattr(StackInterface, "push_back")
    assert hasattr(StackInterface, "pop_back")

    assert issubclass(Stack, StackInterface)
    s = Stack()
    assert hasattr(s, "_top")
    assert s._top is None

    assert isinstance(StackObj, object)
    o1 = StackObj("1")
    assert hasattr(o1, "_data")
    assert hasattr(o1, "_next")
    o2 = StackObj("2")
    o3 = StackObj("3")
    assert hasattr(s, "push_back")
    assert hasattr(s, "pop_back")
    s.push_back(o1)
    assert s._top == o1
    s.push_back(o2)
    assert s._top == o2
    s.push_back(o3)
    assert s._top == o3
    assert s.pop_back() == o3
    assert s._top == o2
    assert s.pop_back() == o2
    assert s._top == o1
    assert s.pop_back() == o1
    assert s._top is None
