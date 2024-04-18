class Car:
    @staticmethod
    def check(value: str) -> bool:
        return isinstance(value, str) and 2 <= len(value) <= 100

    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, value: str) -> None:
        if self.check(value):
            self.__model = value


name = "Toyota"
car = Car()
car.model = name
assert car.model == name
car.model = "s"
assert car.model == name
car.model = 1  # type: ignore
assert car.model == name
car.model = "Ford"
assert car.model == "Ford"
