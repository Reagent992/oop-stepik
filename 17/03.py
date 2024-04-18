from string import ascii_lowercase, digits


class CardCheck:
    """для проверки корректности информации на пластиковых картах."""

    CARD_NUMBER_LEN = 16
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @classmethod
    def check_card_number(cls, number: str) -> bool:
        """проверяет строку с номером карты"""
        number = number.replace("-", "", 3)
        return len(number) == cls.CARD_NUMBER_LEN and set(number) <= set(
            digits
        )

    @classmethod
    def check_name(cls, name: str) -> bool:
        """проверяет строку name с именем пользователя карты."""
        return all(
            [set(i) <= set(cls.CHARS_FOR_NAME) for i in name.split(" ", 1)]
        )


is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")
assert is_number is True
assert is_name is True
