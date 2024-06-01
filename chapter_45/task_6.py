from abc import ABC, abstractmethod


class CountryInterface(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def population(self):
        pass

    @property
    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def get_info(self):
        pass


class Country(CountryInterface):
    def __init__(self, name: str, population: int, square: int) -> None:
        self._name = name
        self._population = population
        self._square = square

    @property
    def name(self) -> str:
        return self._name

    @property
    def population(self) -> int:
        return self._population

    @population.setter
    def population(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError
        if not value > 0:
            raise ValueError
        self._population = value

    @property
    def square(self) -> int:
        return self._square

    @square.setter
    def square(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError
        if not value > 0:
            raise ValueError
        self._square = value

    def get_info(self) -> str:
        return f"{self.name}: {self.square}, {self.population}"


if __name__ == "__main__":
    assert issubclass(CountryInterface, ABC)
    assert hasattr(CountryInterface, "name")
    assert type(CountryInterface.name) == property
    assert hasattr(CountryInterface, "population")
    assert type(CountryInterface.population) == property
    assert hasattr(CountryInterface, "square")
    assert type(CountryInterface.square) == property
    assert hasattr(CountryInterface, "get_info")
    assert callable(CountryInterface.get_info)

    assert issubclass(Country, CountryInterface)
    assert hasattr(Country, "name")
    assert type(Country.name) == property
    assert hasattr(Country, "population")
    assert type(Country.population) == property
    assert hasattr(Country, "square")
    assert type(Country.square) == property
    assert hasattr(Country, "get_info")
    assert callable(Country.get_info)

    obj = Country("Russia", 144, 700)
    assert obj.name == "Russia"
    assert obj.population == 144
    assert obj.square == 700
    obj.population = 120
    assert obj.population == 120
    obj.square = 10
    assert obj.square == 10
    assert obj.get_info() == f"{obj.name}: {obj.square}, {obj.population}"
