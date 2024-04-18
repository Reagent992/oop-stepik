from typing import List, Union


class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year

    @staticmethod
    def validate(title: str, author: str, year: int) -> bool:
        return (
            isinstance(title, str)
            and isinstance(author, str)
            and isinstance(year, int)
        )


class Lib:
    def __init__(self, *books: Union[Book, List[Book]]) -> None:
        self.book_list: List[Book] = []
        if books:
            self.validate(*books)
            if len(books) > 1:
                self.book_list = list(books)  # type: ignore
            elif len(books) == 1:
                self.book_list.append(books[0])  # type: ignore

    def __add__(self, value: Book) -> "Lib":
        self.validate(value)
        self.book_list.append(value)
        return self

    def __sub__(self, value: Union[Book, int]) -> "Lib":
        if type(value) is Book:
            self.validate(value)
            self.book_list.remove(value) if value in self.book_list else None
        elif type(value) is int:
            if len(self.book_list) - 1 >= value:
                self.book_list.pop(value)
        return self

    def __len__(self) -> int:
        return len(self.book_list)

    @staticmethod
    def validate(*books) -> bool:
        result = all(type(book) is Book for book in books)
        if result:
            return True
        raise ValueError


if __name__ == "__main__":
    book1 = Book("title", "author", 1984)
    book2 = Book("title2", "author2", 1984)
    book3 = Book("title3", "author3", 1984)

    lib = Lib()
    assert lib.book_list == []
    lib1 = Lib(book1)
    assert lib1.book_list == [book1]
    lib2 = Lib(book1, book2)
    assert lib2.book_list == [book1, book2]

    # Суммирование
    lib2 = lib2 + book3
    assert lib2.book_list == [book1, book2, book3]

    # Вычитание(удаление по объекту)
    lib2 = lib2 - book3
    assert lib2.book_list == [book1, book2]

    # Вычитание(удаление по индексу)
    lib2 = lib2 - 1
    assert lib2.book_list == [book1]
    lib1 = lib1 - 0
    assert lib1.book_list == []

    # len
    assert len(lib2) == 1
    assert len(lib1) == 0
