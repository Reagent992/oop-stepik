class WordString:
    def __init__(self, string: str = "") -> None:
        self.__string = string

    @property
    def string(self) -> str:
        return self.__string

    @string.setter
    def string(self, value: str) -> None:
        self.__string = value

    def __len__(self) -> int:
        return len(self.__string.split())

    def __call__(self, index_: int) -> str:
        return self.__string.split()[index_]


if __name__ == "__main__":
    w0 = WordString()
    assert len(w0) == 0
    w1 = WordString()
    w1.string = "string"
    assert len(w1) == 1
    w2 = WordString()
    w2.string = "string string string"
    assert len(w2) == 3
    w4 = WordString("string1 string2 string3")
    assert w4(1) == "string2"
