from typing import List

stich = [
    "Я к вам пишу – чего же боле?",
    "Что я могу еще сказать?",
    "Теперь, я знаю, в вашей воле",
    "Меня презреньем наказать.",
    "Но вы, к моей несчастной доле",
    "Хоть каплю жалости храня,",
    "Вы не оставите меня.",
]
for index in range(len(stich)):
    while any(i in stich[index] for i in "–?!,.;"):
        for symbol in "–?!,.;":
            stich[index] = stich[index].replace(symbol, "")


class StringText:
    def __init__(self, words_list: List[str]) -> None:
        self.words_list = words_list

    def __len__(self) -> int:
        return len(self.words_list)

    def __gt__(self, value: "StringText") -> bool:
        return len(self) > len(value)

    def __ge__(self, value: "StringText") -> bool:
        return len(self) >= len(value)

    def __lt__(self, value: "StringText") -> bool:
        return len(self) < len(value)

    def __le__(self, value: "StringText") -> bool:
        return len(self) <= len(value)


lst_text = [StringText(string.split()) for string in stich]
lst_text_sorted = []
for i in sorted(lst_text, key=len, reverse=True):
    lst_text_sorted.append(" ".join(i.words_list))


if __name__ == "__main__":
    assert all(
        [[True if i in _ else False for i in "–?!,.;"] for _ in stich]
    ), "в stich есть знаки которые нужно удалить - (–?!,.;)"
    assert len(lst_text) == 7 and all(
        True if isinstance(_, StringText) else False for _ in lst_text
    ), "ошибка в lst_text"

    assert lst_text_sorted == [
        "Я к вам пишу чего же боле",
        "Теперь я знаю в вашей воле",
        "Но вы к моей несчастной доле",
        "Что я могу еще сказать",
        "Хоть каплю жалости храня",
        "Вы не оставите меня",
        "Меня презреньем наказать",
    ], "неверно отсортирован список lst_text_sorted"

    assert (
        lst_text[0] > lst_text[4] and lst_text[4] > lst_text[1]
    ), "метод > работает неверно"
    assert lst_text[1] < lst_text[4], "метод < работает неверно"

    assert lst_text[2] >= lst_text[4], "метод >= работает неверно"
    assert lst_text[2] <= lst_text[4], "метод >= работает неверно"

    print("Правильный ответ.")
