from typing import Optional


class StackObj:
    """Obj of Stack."""

    def __init__(self, data: str, next: Optional["StackObj"] = None) -> None:
        self.data = data
        self.next = next


class Stack:

    def __init__(self, top: Optional["StackObj"] = None) -> None:
        self.top = top
        self.end: Optional[StackObj] = None

    def push_back(self, value: StackObj) -> None:
        """Addend new StackObj."""
        self.validate_stack_obj(value)
        if self.end:
            self.end.next = value
            self.end = value
        elif self.top:
            self.end = value
            self.top.next = value
        else:
            self.top = value

    def push_front(self, value: StackObj) -> None:
        """AddFront new StackObj."""
        self.validate_stack_obj(value)
        if self.top:
            cur_top = self.top
            self.top = value
            self.top.next = cur_top
        else:
            self.top = value

    def __getitem__(self, index: int) -> str:
        if not self.top or index < 0:
            raise IndexError("неверный индекс")
        return self.get_obj_by_index(index).data

    def __setitem__(self, index: int, value: str) -> None:
        obj = self.get_obj_by_index(index)
        obj.data = value

    def get_obj_by_index(self, index: int) -> StackObj:
        if not self.top or index < 0:
            raise IndexError("неверный индекс")
        cur_obj = self.top
        for _ in range(index):
            if cur_obj.next:
                cur_obj = cur_obj.next
            else:
                raise IndexError("неверный индекс")
        return cur_obj

    def __len__(self) -> int:
        if not self.top:
            return 0
        cur_obj = self.top
        len = 1
        while cur_obj.next:
            len += 1
            cur_obj = cur_obj.next
        return len

    def __iter__(self):
        self.cur_iter_value = self.top
        return self

    def __next__(self):
        if self.cur_iter_value:
            obj = self.cur_iter_value
            self.cur_iter_value = self.cur_iter_value.next
            return obj
        else:
            raise StopIteration

    @staticmethod
    def validate_stack_obj(value: StackObj) -> bool:
        if not isinstance(value, StackObj):
            raise ValueError("Wrong arg passed")
        return True


if __name__ == "__main__":
    # StackObj
    so1 = StackObj("1")
    so2 = StackObj("2")
    so3 = StackObj("3")
    so4 = StackObj("4")
    # Stack
    stack = Stack()
    stack.push_front(so1)
    assert stack.top == so1
    stack.push_back(so2)
    assert stack.end == so2
    stack.push_back(so3)
    assert stack.end == so3 and stack.top == so1
    stack.push_front(so4)
    assert stack.top == so4
    cur_obj = stack.top
    for i in (so4, so1, so2, so3):
        assert cur_obj == i
        cur_obj = cur_obj.next  # type: ignore
    # getitem
    assert stack[0] == so4.data
    assert stack[3] == so3.data
    assert stack[1] == so1.data
    try:
        stack[4]
    except IndexError:
        assert True
    else:
        assert False, "Must be IndexError"
    try:
        stack[-1]
    except IndexError:
        assert True
    else:
        assert False, "Must be IndexError"
    # setitem
    stack[0] = "20"
    stack[3] = "30"
    assert stack[0] == "20" and stack[3] == "30"
    # len
    assert len(stack) == 4
    assert len(Stack()) == 0
    # iter and next
    assert [i for i in stack] == [so4, so1, so2, so3]
    assert [i for i in Stack()] == []
