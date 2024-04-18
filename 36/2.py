import sys
from typing import Dict, List, Union


class ShopItem:
    def __init__(
        self, name: str, weight: Union[int, float], price: Union[int, float]
    ) -> None:
        self.name = name
        self.weight = weight
        self.price = price

    def __eq__(self, obj: "ShopItem") -> bool:  # type: ignore
        return hash(self) == hash(obj)

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))


test_text = """
Системный блок: 1500 75890.56
Монитор Samsung: 2000 34000
Клавиатура: 200.44 545
Монитор Samsung: 2000 34000
"""
TEST = False
if TEST:
    lst_in = test_text.strip().split("\n")
else:
    lst_in = list(map(str.strip, sys.stdin.readlines()))
shop_items: Dict[ShopItem, List[Union[ShopItem, int]]] = {}
for item in lst_in:
    t = item.split()
    obj = ShopItem(" ".join(t[:-2]), float(t[-2]), float(t[-1]))
    if obj in shop_items:
        shop_items[obj][1] += 1  # type: ignore
    else:
        shop_items[obj] = [obj, 1]
