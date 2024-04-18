from typing import Tuple


class Morph:
    """Морфология."""

    def __init__(self, *words: str) -> None:
        self.__words = list(words)

    def add_word(self, word: str) -> None:
        """Добавление нового(уникального) слова."""
        self.__words.append(word) if word not in self.__words else None

    def get_words(self) -> Tuple[str, ...]:
        """Получение кортежа форм слов."""
        return tuple(self.__words)

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, str):
            return any(__value.lower() == i.lower() for i in self.__words)
        raise NotImplementedError


s = """- связь, связи, связью, связи, связей, связям, связями, связях
- формула, формулы, формуле, формулу, формулой, формул, формулам, формулами, формулах
- вектор, вектора, вектору, вектором, векторе, векторы, векторов, векторам, векторами, векторах
- эффект, эффекта, эффекту, эффектом, эффекте, эффекты, эффектов, эффектам, эффектами, эффектах
- день, дня, дню, днем, дне, дни, дням, днями, днях
"""

dict_words = [Morph(*line.lstrip("- ").split(", ")) for line in s.splitlines()]


def main(text):
    count = 0
    for i in text.rstrip(".").split():
        for word in dict_words:
            if i == word:
                count += 1
    return count


TEST = False
if not TEST:
    print(main(input()))


if __name__ == "__main__":
    w1 = Morph("абв", "абвг", "абвгд")
    assert (w1 == "абв") is True
    assert (w1 == "а") is False
    assert (w1 != "г") is True
    assert ("абвг" == w1) is True
    assert main("Мы будем устанавливать связь завтра днем.") == 2
