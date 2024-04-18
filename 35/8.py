from typing import List, Union


class Thing:
    def __init__(self, name: str, mass: Union[int, float]) -> None:
        self.name = name
        self.mass = mass

    def __eq__(self, __value: "Thing") -> bool:  # type: ignore
        return (
            self.name.lower() == __value.name.lower()
            and self.mass == __value.mass
        )


class Box:
    def __init__(self) -> None:
        self.__storage: List[Thing] = list()

    def add_thing(self, *obj: Thing) -> None:
        for i in obj:
            if isinstance(i, Thing):
                self.__storage.append(i)

    def get_things(self) -> List[Thing]:
        return self.__storage

    def __eq__(self, obj: "Box") -> bool:  # type: ignore
        if len(self.__storage) != len(obj.__storage):
            return False
        if sorted(self.__storage, key=lambda x: x.name) == sorted(
            obj.__storage, key=lambda x: x.name
        ):
            return True
        return False


if __name__ == "__main__":
    t1 = Thing("abc", 10)
    t2 = Thing("abc", 10)
    t3 = Thing("abc", 20)
    assert (t1 == t2) is True
    assert (t2 != t3) is True

    b1 = Box()
    b1.add_thing(t1, t2, t3)

    b2 = Box()
    b2.add_thing(t1, t2, t3)

    b3 = Box()
    b3.add_thing(t1, t2)

    assert (b1 == b2) is True
    assert (b1 != b3) is True
