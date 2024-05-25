class StringDigit(str):
    def __init__(self, value: str) -> None:
        if not value.isdigit():
            raise ValueError
        super().__init__()

    def __add__(self, value: str) -> "StringDigit":
        return StringDigit(str(self) + value)

    def __radd__(self, value: str) -> "StringDigit":
        return StringDigit(value + str(self))


if __name__ == "__main__":
    try:
        string = StringDigit("abc")
    except ValueError:
        assert True
    else:
        assert False
    string = StringDigit("123")
    assert string == "123"

    new_string = string + "456"
    assert new_string == "123456"
    assert type(new_string) == StringDigit

    new_string = "456" + string
    assert new_string == "456123"
    assert type(new_string) == StringDigit
