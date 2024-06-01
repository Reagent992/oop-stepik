from typing import Callable, Optional, Tuple, Type, Union


class Descriptor:
    def __init__(
        self, validator: Optional[Callable] = None, exception=ValueError
    ) -> None:
        self.validator = validator
        self.exception = exception

    def __set_name__(self, owner: Type[object], name: str):
        self.private_name = f"_{owner.__name__}__{name}"

    def __get__(self, obj: object, objtype=None):
        return getattr(obj, self.private_name, None)

    def __set__(self, obj: object, value) -> None:
        if self.validator is not None:
            if self.validator(value):
                setattr(obj, self.private_name, value)


def digit_validator(value: Union[int, float]) -> bool:
    if not isinstance(value, (int, float)):
        raise TypeError
    return True


class PointTrack:
    x = Descriptor(digit_validator)
    y = Descriptor(digit_validator)

    def __init__(self, x: Union[int, float], y: Union[int, float]) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self.x}, {self.y}"


class Track:
    def __init__(
        self,
        *args: Union[Union[int, float], PointTrack],
    ) -> None:
        if len(args) == 2 and all(isinstance(i, (int, float)) for i in args):
            self.__points = [PointTrack(*args)]  # type: ignore
        else:
            self.__points = list(args)  # type: ignore

    @property
    def points(self) -> Tuple[PointTrack, ...]:
        return tuple(self.__points)

    def add_front(self, pt: PointTrack) -> None:
        self.__points.insert(0, pt)

    def add_back(self, pt: PointTrack) -> None:
        self.__points.append(pt)

    def pop_back(self) -> PointTrack:
        return self.__points.pop()

    def pop_front(self) -> PointTrack:
        return self.__points.pop(0)


if __name__ == "__main__":
    assert isinstance(PointTrack, object)
    p1 = PointTrack(1, 2)
    assert p1.x == 1
    assert p1.y == 2
    try:
        PointTrack("a", "b")  # type: ignore
    except TypeError:
        assert True
    else:
        assert False

    assert str(p1) == f"{p1.__class__.__name__}: {p1.x}, {p1.y}"

    assert isinstance(Track, object)
    assert type(Track.points) == property
    t1 = Track(0, 0)
    assert hasattr(t1, "_Track__points")
    assert isinstance(t1._Track__points[0], PointTrack)

    p2 = PointTrack(3, 4)
    t2 = Track(p1, p2)
    assert all(isinstance(i, PointTrack) for i in t2._Track__points)  # type: ignore

    assert hasattr(t1, "points")
    assert t2.points == (p1, p2)
    assert hasattr(t1, "add_front")
    assert hasattr(t1, "add_back")
    assert hasattr(t1, "pop_back")
    assert hasattr(t1, "pop_front")
    t3 = Track()
    assert t3.points == ()
    t3.add_back(p1)
    assert t3.points == (p1,)
    assert t3.pop_back() == p1
    assert t3.points == ()
    t3.add_front(p1)
    t3.add_front(p2)
    assert t3.points == (p2, p1)
    assert t3.pop_front() == p2
