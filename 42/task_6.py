from typing import Iterator, Tuple


class IteratorAttrs:
    def __iter__(self) -> Iterator:
        yield from self.__dict__.items()


class SmartPhone(IteratorAttrs):
    def __init__(self, model: str, size: Tuple[int, int], memory: int) -> None:
        self.model = model
        self.size = size
        self.memory = memory


if __name__ == "__main__":
    phone = SmartPhone("nokia", (10, 20), 64)
    for key, value in phone:
        print(key, value)
# model nokia
# size (10, 20)
# memory 64

