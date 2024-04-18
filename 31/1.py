class Book:
    def __init__(
        self, title: str = "", author: str = "", pages: int = 0, year: int = 0
    ):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if key in ("title", "author") and isinstance(value, str):
            super().__setattr__(key, value)
        elif key in ("pages", "year") and isinstance(value, int):
            super().__setattr__(key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")


book = Book("Python ООП", "Сергей Балакирев", 123, 2022)
