from typing import Any, Dict, Optional


class Thing:
    def __init__(self, name: str, price: float, weight: float) -> None:
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self) -> int:
        return hash((self.name, self.price, self.weight))


class DictShop(dict):
    def __init__(self, key: Optional[Dict["Thing", Any]] = None) -> None:
        if key is not None:
            self.validate(key)
            super().__init__(key)

    @classmethod
    def validate(cls, key: Dict["Thing", Any]) -> bool:
        if not isinstance(key, dict):
            raise TypeError("must be dict")
        cls.validate_keys(*key.keys())
        return True

    @classmethod
    def validate_keys(cls, *values: "Thing") -> bool:
        if not all(isinstance(i, Thing) for i in values):
            raise TypeError("keys must be Thing obj")
        return True

    def __setitem__(self, index: Thing, value: Any) -> None:
        self.validate_keys(index)
        super().__setitem__(index, value)


if __name__ == "__main__":
    t = Thing("a", 1.0, 100.0)
    t2 = Thing("b", 11.1, 11.1)
    assert hash(t)

    d = DictShop({t: t})
    d[t2] = t2
    assert d[t2] == t2

