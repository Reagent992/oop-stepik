from typing import Optional, Union


T = Optional[Union[int, float]]


class Ellipse:

    def __init__(
        self, x1: T = None, y1: T = None, x2: T = None, y2: T = None
    ) -> None:
        if x1:
            setattr(self, "x1", x1)
        if x2:
            setattr(self, "x2", x2)
        if y1:
            setattr(self, "y1", y1)
        if y2:
            setattr(self, "y2", y2)
        self.array = [
            getattr(self, "x1", None),
            getattr(self, "y1", None),
            getattr(self, "x2", None),
            getattr(self, "y2", None),
        ]

    def __bool__(self) -> bool:
        return all([type(i) is not type(None) for i in self.array])

    def get_coords(self):
        if bool(self):
            return tuple(self.array)
        else:
            raise AttributeError("нет координат для извлечения")


lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 1, 2, 2), Ellipse(1, 1, 2, 2)]
for i in lst_geom:
    if i:
        i.get_coords()

if __name__ == "__main__":
    e1 = Ellipse()
    try:
        e1.get_coords()
    except AttributeError as e:
        assert e

    assert hasattr(e1, "x1") is False

    e2 = Ellipse(1, 2, 3, 4)
    try:
        e2.get_coords()
    except AttributeError:
        raise Exception

    assert e2.get_coords() == (1, 2, 3, 4)
