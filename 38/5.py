from typing import List, Optional


class StackObj:
    def __init__(self, data: str) -> None:
        self.data = data
        self.next: Optional["StackObj"] = None


class Stack:
    def __init__(self) -> None:
        self.top: Optional["StackObj"] = None
        self.stack: List[StackObj] = []

    def push(self, obj: StackObj) -> None:
        if self.top:
            self.stack[-1].next = obj
        if not self.top:
            self.top = obj
        self.validate_obj(obj)
        self.stack.append(obj)

    def pop(self) -> StackObj:
        obj = self.stack.pop()
        if len(self.stack) > 1:
            self.stack[-1].next = None
        if len(self.stack) == 0:
            self.top = None
        return obj

    def validate_obj(self, obj: StackObj) -> bool:
        if not isinstance(obj, StackObj):
            raise ValueError("Wrong class passed")
        return True

    def __getitem__(self, index: int) -> StackObj:
        self.validate_index(index)
        return self.stack[index]

    def __setitem__(self, index: int, new_value: StackObj) -> None:
        self.validate_index(index)
        old_next_for_cur_index = self.stack[index].next
        self.stack[index] = new_value
        self.stack[index].next = old_next_for_cur_index
        if index != 0:
            self.stack[index - 1].next = new_value

    def validate_index(self, index: int) -> bool:
        if not -len(self.stack) <= index <= len(self.stack) - 1:
            raise IndexError("неверный индекс")
        return True


if __name__ == "__main__":
    so1 = StackObj("1")
    so2 = StackObj("2")
    so3 = StackObj("3")
    so4 = StackObj("4")
    assert so1.data == "1"
    assert so2.data == "2"
    assert so3.data == "3"

    # stack work
    stack1 = Stack()
    assert stack1.top is None
    stack1.push(so1)
    assert stack1.top == so1
    assert stack1.stack == [so1]
    stack1.push(so2)
    assert so1.next == so2
    assert stack1.top == so1
    assert stack1.stack == [so1, so2]
    stack1.push(so3)
    assert stack1.pop() == so3
    assert stack1.top == so1
    assert stack1.stack == [so1, so2]
    assert stack1.pop() == so2
    assert stack1.top == so1
    assert stack1.stack == [so1]
    assert stack1.pop() == so1
    assert stack1.top is None
    assert stack1.stack == []

    # stack index work
    stack2 = Stack()
    for obj in (so1, so2, so3):
        stack2.push(obj)
    stack2[1] = so4
    assert stack2[0].next == so4
    assert stack2[1].next == so3
