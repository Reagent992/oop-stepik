import sys

# здесь пишите программу

lst_in = list(
    map(str.strip, sys.stdin.readlines())
)  # считывание списка из входного потока (эту строчку не менять)


class Book:
    def __init__(self, title: str, author: str, pages: str) -> None:
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        return f"Книга: {self.title}; {self.author}; {self.pages}"


book = Book(title=lst_in[0], author=lst_in[1], pages=lst_in[2])
print(book)
