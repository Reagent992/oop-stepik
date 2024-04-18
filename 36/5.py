from typing import Union


class Dimensions:

    def __init__(
        self, a: Union[int, float], b: Union[int, float], c: Union[int, float]
    ) -> None:
        if self.validate(a, b, c):
            self.a = a
            self.b = b
            self.c = c
        else:
            raise ValueError(
                "габаритные размеры должны быть положительными числами"
            )

    def __hash__(self) -> int:
        return hash((self.a, self.b, self.c))

    @staticmethod
    def validate(*values: Union[int, float]) -> bool:
        return all(
            isinstance(value, (int, float)) and value > 0 for value in values
        )


if __name__ == "__main__":
    s_inp = input()
    lst_dims = sorted(
        [
            Dimensions(*map(float, string.split()))
            for string in s_inp.split("; ")
        ],
        key=lambda x: hash(x),
    )
