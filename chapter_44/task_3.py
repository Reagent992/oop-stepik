from typing import Any, Dict


class Observer:
    def update(self, data) -> None:
        pass

    def __hash__(self) -> int:
        return hash(id(self))


class Subject:
    def __init__(self) -> None:
        self.__observers: Dict[Observer, Any] = {}
        self.__data = None

    def add_observer(self, observer: Observer) -> None:
        self.__observers[observer] = observer

    def remove_observer(self, observer) -> None:
        if observer in self.__observers:
            self.__observers.pop(observer)

    def __notify_observer(self) -> None:
        for ob in self.__observers:
            ob.update(self.__data)

    def change_data(self, data) -> None:
        self.__data = data
        self.__notify_observer()


class Data:
    def __init__(self, temp, press, wet) -> None:
        self.temp = temp  # температура
        self.press = press  # давление
        self.wet = wet  # влажность


# здесь объявляйте дочерние классы TemperatureView, PressureView и WetView
class TemperatureView(Observer):
    def update(self, data: Data) -> None:
        print(f"Текущая температура {data.temp}")


class PressureView(Observer):
    def update(self, data: Data) -> None:
        print(f"Текущее давление {data.press}")


class WetView(Observer):
    def update(self, data: Data) -> None:
        print(f"Текущая влажность {data.wet}")

if __name__ == '__main__':
    subject = Subject()
    tv = TemperatureView()
    pr = PressureView()
    wet = WetView()

    subject.add_observer(tv)
    subject.add_observer(pr)
    subject.add_observer(wet)

    subject.change_data(Data(23, 150, 83))
    # выведет строчки:
    # Текущая температура 23
    # Текущее давление 150
    # Текущая влажность 83
    subject.remove_observer(wet)
    subject.change_data(Data(24, 148, 80))
    # выведет строчки:
    # Текущая температура 24
    # Текущее давление 148
