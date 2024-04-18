from random import choice, randint
import re
from string import ascii_letters, digits


class EmailValidator:
    """Проверка корректности email-адреса."""

    def __new__(cls):
        """Запрещено создавать экземпляры класса."""
        return None

    @classmethod
    def get_random_email(cls) -> str:
        """Генерация случайного email-адресса."""
        valid_symbols = ascii_letters + digits + "-_"
        return (
            "".join([choice(valid_symbols) for _ in range(randint(1, 100))])
            + "@gmail.com"
        )

    @classmethod
    def check_email(cls, email: str) -> bool:
        """Проверка корректности email."""
        if not cls.__is_email_str(email):
            return False
        pattern = r"(?a)(?!.*\.\..*)[\w.-]{1,100}@(?=.*\.)[\w.-]{1,50}"
        match = re.fullmatch(pattern, email)
        return bool(match)

    @staticmethod
    def __is_email_str(email: str):
        return isinstance(email, str)


assert EmailValidator() is None
# Проверка get_random_email
regexp = r"(?P<first_half>[0-9A-Za-z\d_-]+)@gmail\.com"
m = re.fullmatch(regexp, EmailValidator.get_random_email())
assert bool(m) is True
if m:
    assert 1 <= len(m.group("first_half")) <= 100
# Проверка check_email
assert EmailValidator.check_email("sc_lib@list.ru") is True
assert EmailValidator.check_email("sc_lib@list_ru") is False
assert EmailValidator.check_email("@list.ru") is False
assert EmailValidator.check_email("asdsa..asd@list.ru") is False
assert EmailValidator.check_email("asdsa..asd@list..ru") is False
# 3
t = EmailValidator.get_random_email()
assert EmailValidator.check_email(t) is True, f"{t} не прошел проверку"
