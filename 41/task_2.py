from typing import Optional, Tuple, Union
from uuid import uuid4


class Thing:
    def __init__(self, name: str, price: int) -> None:
        self.id = uuid4().int
        self.name = name
        self.price = price
        self.weight: Optional[Union[int, float]] = None
        self.dims: Optional[Tuple[int, int, int]] = None
        self.memory: Optional[int] = None
        self.frm: Optional[str] = None

    def get_data(self) -> Tuple:
        return (
            self.id,
            self.name,
            self.price,
            self.weight,
            self.dims,
            self.memory,
            self.frm,
        )


class Table(Thing):
    def __init__(
        self,
        name: str,
        price: int,
        weight: Union[int, float],
        dims: Tuple[int, int, int],
    ) -> None:
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims


class ElBook(Thing):
    def __init__(self, name: str, price: int, memory: int, frm: str) -> None:
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm
