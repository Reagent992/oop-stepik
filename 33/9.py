from typing import List, Tuple


class Descriptor_for_coords:

    def __set_name__(self, owner: "PolyLine", name: str) -> None:
        self.private_name: str = f"_{owner.__name__}__{name}"  # type: ignore

    def __get__(self, obj: "PolyLine", objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj: "PolyLine", value: List[Tuple[int, int]]) -> None:
        if self.validate(value):
            setattr(obj, self.private_name, value)
        else:
            raise ValueError("Передан неверный формат данных.")

    def validate(self, value: List[Tuple[int, int]]) -> bool:
        return (
            isinstance(value, list)
            and all(isinstance(i, tuple) for i in value)
            and all((isinstance(x, int) for x in i) for i in value)
        )


class PolyLine:
    """Полилиния."""

    coords = Descriptor_for_coords()

    def __init__(
        self,
        *args: Tuple[int, int],
    ) -> None:
        self.coords: List[Tuple[int, int]] = list(args)  # type: ignore

    def add_coord(self, x: int, y: int) -> None:
        """Добавление новой координаты в конец."""
        new_coord = (x, y)
        if self.validate(*new_coord):
            self.coords.append(new_coord)
        else:
            raise ValueError("Передан неверный формат данных.")

    def remove_coord(self, index_: int) -> None:
        """удаление координаты по индексу."""
        self.coords.pop(index_)

    def get_coords(self) -> Tuple[Tuple[int, int]]:
        """Получение списка координат (в виде списка из кортежей)."""
        return tuple(self.coords)  # type: ignore

    @staticmethod
    def validate(*args: int) -> bool:
        return all(isinstance(i, int) for i in args)


if __name__ == "__main__":
    # Проверка создания Полилинии.
    p_line1 = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
    assert p_line1.coords == [(1, 2), (3, 5), (0, 10), (-1, 8)]

    # Проверка add_coord
    p_line1.add_coord(5, 6)
    assert p_line1.coords == [(1, 2), (3, 5), (0, 10), (-1, 8), (5, 6)]

    # Проверка get_coords
    assert p_line1.get_coords() == ((1, 2), (3, 5), (0, 10), (-1, 8), (5, 6))
