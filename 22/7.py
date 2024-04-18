from typing import List


class PhoneBook:
    phone_book: List["PhoneNumber"] = list()

    @classmethod
    def add_phone(cls, phone: "PhoneNumber"):
        """Добавление нового номера телефона (в список)."""
        cls.phone_book.append(phone)

    @classmethod
    def remove_phone(cls, indx: int):
        """Удаление номера телефона по индексу списка."""
        del cls.phone_book[indx]

    @classmethod
    def get_phone_list(cls):
        """Получение списка из объектов всех телефонных номеров."""
        return cls.phone_book


class PhoneNumber:
    def __init__(self, number: int, fio: str) -> None:
        self.number = number
        self.fio = fio


if __name__ == "__main__":
    p = PhoneBook()
    p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
    p.add_phone(PhoneNumber(21345678901, "Панда"))
    p.remove_phone(0)
    phones = p.get_phone_list()
    print(phones)
