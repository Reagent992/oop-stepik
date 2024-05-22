from typing import Dict, List, Union


class SellItem:
    def __init__(self, name: str, price: Union[int, float]) -> None:
        self.name = name
        self.price = price

    def __hash__(self) -> int:
        return hash((self.name, self.price))

    def __eq__(self, value: object) -> bool:
        return hash(self) == hash(value)

    @staticmethod
    def validate(obj: "SellItem") -> bool:
        if not isinstance(obj, SellItem):
            raise ValueError
        return True


class Flat(SellItem):
    def __init__(
        self,
        name: str,
        price: Union[int, float],
        size: Union[int, float],
        rooms: int,
    ) -> None:
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms


class House(SellItem):
    def __init__(
        self, name: str, price: Union[int, float], material: str, square: float
    ) -> None:
        super().__init__(name, price)
        self.material = material
        self.square = square


class Land(SellItem):
    def __init__(
        self, name: str, price: Union[int, float], square: float
    ) -> None:
        super().__init__(name, price)
        self.square = square


class Agency:
    def __init__(self, name: str) -> None:
        self.name = name
        self.for_sale: Dict[SellItem, SellItem] = dict()

    def add_object(self, obj: SellItem) -> None:
        self.validate(obj)
        self.for_sale[obj] = obj

    def remove_object(self, obj: SellItem) -> None:
        self.validate(obj)
        del self.for_sale[obj]

    def get_objects(self) -> List[SellItem]:
        return [i for i in self.for_sale]

    @staticmethod
    def validate(obj: SellItem) -> bool:
        if not isinstance(obj, SellItem):
            raise ValueError
        return True


if __name__ == "__main__":
    ag = Agency("Рога и копыта")
    ag.add_object(Flat("квартира, 3к", 10000000, 121.5, 3))
    ag.add_object(Flat("квартира, 2к", 8000000, 74.5, 2))
    ag.add_object(Flat("квартира, 1к", 4000000, 54, 1))
    ag.add_object(
        House(
            "дом, крипичный", price=35000000, material="кирпич", square=186.5
        )
    )
    ag.add_object(Land("участок под застройку", 3000000, 6.74))
    for obj in ag.get_objects():
        print(obj.name)

    lst_houses = [
        x for x in ag.get_objects() if isinstance(x, House)
    ]  # выделение списка домов
