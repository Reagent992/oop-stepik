from typing import List, Tuple, Union

INDEX = Union[int, slice]


class RadiusVector:
    def __init__(self, *args: int) -> None:
        self.coords = list(args)

    def __getitem__(self, index: INDEX) -> Union[int, Tuple[int, ...]]:
        self.validate_indexes(index)
        if isinstance(index, int):
            return self.coords[index]
        if isinstance(index, slice):
            return tuple(self.coords[index])

    def __setitem__(self, index: INDEX, value) -> None:
        self.validate_indexes(index) and self.validate_value(value)
        self.coords[index] = value

    def validate_indexes(self, index: INDEX) -> bool:
        if isinstance(index, int) and (
            -len(self.coords) <= index <= len(self.coords) - 1
        ):
            return True
        elif (
            isinstance(index, slice)
            # and (-len(self.coords) <= index.start <= len(self.coords) - 1)
            # and (-len(self.coords) <= index.stop <= len(self.coords) - 1)
        ):
            return True
        raise IndexError

    @staticmethod
    def validate_value(values: Union[int, List[int]]) -> bool:
        if isinstance(values, list) and not all(
            isinstance(value, int) for value in values
        ):
            raise ValueError
        return True


if __name__ == "__main__":
    # create Radius
    r1 = RadiusVector(1, 2, 3, 4)
    # get one index
    assert r1[0] == 1 and r1[3] == 4 and r1[-2] == 3
    try:
        r1[10]
    except IndexError:
        assert True
    else:
        assert False, "must be raise IndexError"
    # slice
    assert r1[0:2] == (1, 2)
    assert r1[-3:-1] == (2, 3)
    assert r1[-3:-1:2] == (2,)
    # set
    r1[0] = 10
    assert r1[0] == 10
    # set slice
    r1[0:2] = [5, 6]
    assert r1[0:2] == (5, 6)
    r1[0:4:2] = [11, 12]
    assert r1[0:4:2] == (11, 12)
