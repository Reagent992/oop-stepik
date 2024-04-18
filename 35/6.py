from typing import Optional, Union
import abc


class CentralBank:
    """Центральный банк."""

    rates = {"rub": 72.5, "dollar": 1.0, "euro": 1.15}

    def __new__(cls):
        return None

    @classmethod
    def register(cls, *values):
        for value in values:
            value.cb = cls if isinstance(value, MoneyABC) else None


class MoneyABC(abc.ABC):
    """Абстрактный класс денег."""

    def __init__(self, volume: Union[int, float] = 0) -> None:
        self.__cb: Optional[CentralBank] = None
        self.__volume = volume

    @property
    def cb(self) -> Optional[CentralBank]:
        """Центральный банк, чтение."""
        return self.__cb

    @cb.setter
    def cb(self, new_cb: CentralBank) -> None:
        """Центральный банк, запись."""
        self.__cb = new_cb

    @property
    def volume(self) -> Union[int, float]:
        """Кол-во денег, чтение."""
        return self.__volume

    @volume.setter
    def volume(self, value: Union[int, float]) -> None:
        """Кол-во денег, запись."""
        if isinstance(value, (int, float)):
            self.__volume = value

    @abc.abstractmethod
    def get_rub_value(self) -> Union[float, int]:
        pass

    def __gt__(
        self, value: Union["MoneyABC", "MoneyD", "MoneyE"]
    ) -> Optional[bool]:
        """Сравнение валют по курсу ЦБ."""
        if self.get_rub_value() and value.get_rub_value():
            return self.get_rub_value() > value.get_rub_value()
        else:
            return None

    def __eq__(self, value: object) -> bool:
        if isinstance(value, MoneyABC):
            return (
                self.get_rub_value() == value.get_rub_value()
                or abs(self.get_rub_value() - value.get_rub_value()) <= 0.1
            )
        raise ValueError

    def __ge__(
        self, value: Union["MoneyABC", "MoneyD", "MoneyE"]
    ) -> Optional[bool]:
        """Сравнение валют по курсу ЦБ."""
        if self.get_rub_value() and value.get_rub_value():
            return self.get_rub_value() >= value.get_rub_value()
        else:
            return None


class MoneyR(MoneyABC):
    """Рублевые кошельки."""

    def get_rub_value(self) -> Union[float, int]:
        """Получение рублевого эквивалента."""
        if self.cb is not None:
            return self.volume
        else:
            raise ValueError("Неизвестен курс валют.")


class MoneyD(MoneyABC):
    """Долларовые кошельки."""

    def get_rub_value(self) -> Union[float, int]:
        """Получение рублевого эквивалента."""
        if self.cb is not None:
            return self.cb.rates["rub"] * self.volume
        else:
            raise ValueError("Неизвестен курс валют.")


class MoneyE(MoneyABC):
    """Евро кошельки."""

    def get_rub_value(self) -> Union[float, int]:
        """Получение рублевого эквивалента."""
        if self.cb is not None:
            return self.cb.rates["rub"] * (
                self.volume / self.cb.rates["dollar"]
            )
        else:
            raise ValueError("Неизвестен курс валют.")


if __name__ == "__main__":
    rub1 = MoneyR()
    CentralBank.register(rub1)
    assert rub1.volume == 0

    rub2 = MoneyR(10)
    eur1 = MoneyE(1)
    CentralBank.register(rub2, eur1)
    assert (rub2 < eur1) is True

    rub3 = MoneyR(72.5)
    eur2 = MoneyE(1)
    CentralBank.register(rub3, eur2)
    assert (rub3 == eur2) is True

    rub4 = MoneyR(72.4)
    eur4 = MoneyE(1)
    CentralBank.register(rub4, eur4)
    assert (rub4 == eur4) is True

    rub5 = MoneyR(33)
    eur5 = MoneyE(1)
    CentralBank.register(rub5, eur5)
    assert (rub5 <= eur5) is True
