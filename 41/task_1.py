class Animal:
    def __init__(self, name: str, old: int) -> None:
        self.name = name
        self.old = old


class Cat(Animal):
    def __init__(self, name: str, old: int, color: str, weight: int) -> None:
        super().__init__(name, old)
        self.color = color
        self.weight = weight

    def get_info(self) -> str:
        return f"{self.name}: {self.old}, {self.color}, {self.weight}"


class Dog(Animal):
    def __init__(self, name: str, old: int, breed: str, size: int) -> None:
        super().__init__(name, old)
        self.breed = breed
        self.size = size

    def get_info(self) -> str:
        return f"{self.name}: {self.old}, {self.breed}, {self.size}"


if __name__ == "__main__":
    # Cat
    cat_name = "Vasya"
    cat_age = 3
    cat_color = "black"
    cat_weight = 10
    cat = Cat(cat_name, cat_age, cat_color, cat_weight)
    assert cat.name == cat_name
    assert cat.old == cat_age
    assert cat.color == cat_color
    assert cat.weight == cat_weight
    print(cat.get_info())
