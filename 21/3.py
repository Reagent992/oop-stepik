class Book:
    def __init__(self, author: str, title: str, price: int) -> None:
        self.__author = author
        self.__title = title
        self.__price = price

    def set_title(self, title: str):
        """запись в локальное приватное свойство __title объектов
        класса Book значения title"""
        self.__title = title

    def set_author(self, author: str):
        """запись в локальное приватное свойство __author объектов
        класса Book значения author;"""
        self.__author = author

    def set_price(self, price: int):
        """запись в локальное приватное свойство __price объектов
        класса Book значения price;"""
        self.__price = price

    def get_title(self) -> str:
        """получение значения локального приватного свойства
        __title объектов класса Book;"""
        return self.__title

    def get_author(self) -> str:
        """получение значения локального приватного свойства
        __author объектов класса Book;"""
        return self.__author

    def get_price(self) -> int:
        """получение значения локального приватного свойства
        __price объектов класса Book;"""
        return self.__price


author = "Гоголь"
title = "Дурак"
price = 1999
book = Book(author, title, price)
assert book.get_author() == author
assert book.get_price() == price
assert book.get_title() == title
