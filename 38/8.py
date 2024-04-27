from typing import List


class Bag:
    def __init__(self, max_weight) -> None:
        self.max_weight = max_weight
        self.stash: List["Thing"] = []

    def add_thing(self, thing: "Thing") -> None:
        if isinstance(thing, Thing) and self.validate_weight(thing):
            self.stash.append(thing)

    def __getitem__(self, index: int) -> "Thing":
        self.validate_index(index)
        return self.stash[index]

    def __setitem__(self, index: int, value: "Thing") -> None:
        if not isinstance(value, Thing):
            raise ValueError
        self.validate_index(index)
        self.validate_weight(value, index)
        self.stash[index] = value

    def __delitem__(self, index: int) -> None:
        self.validate_index(index)
        del self.stash[index]

    def validate_weight(self, thing: "Thing", index=None) -> bool:
        stash_sum = sum(i.weight for i in self.stash)
        if index is not None:
            stash_sum -= self.stash[index].weight
        if thing.weight + stash_sum > self.max_weight:
            raise ValueError("превышен суммарный вес предметов")
        return True

    def validate_index(self, index: int) -> bool:
        if not isinstance(index, int) or not -len(self.stash) <= index <= len(
            self.stash
        ):
            raise IndexError("неверный индекс")
        return True


class Thing:
    def __init__(self, name: str, weight: int) -> None:
        self.name = name
        self.weight = weight


if __name__ == "__main__":
    # Thing
    t1 = Thing("book", 100)
    t2 = Thing("phone", 20)
    t3 = Thing("knife", 20)
    assert t1.name == "book" and t1.weight == 100

    # Bag
    # create and get
    b1 = Bag(120)
    b1.add_thing(t1)
    b1.add_thing(t2)
    assert b1[0] == t1 and b1[1] == t2
    try:
        b1.add_thing(t3)
    except ValueError:
        assert True
    else:
        assert False
    # set
    b1[1] = t3
    assert b1[1] == t3
    try:
        b1[2]
    except IndexError:
        assert True
    else:
        assert False
    # del
    del b1[1]
    try:
        b1[1]
    except IndexError:
        assert True
    else:
        assert False
