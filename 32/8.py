from typing import Any


class InputDigits:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, func) -> Any:
        digits = func()
        digits = list(map(int, digits.split()))
        return digits


if __name__ == "__main__":

    @InputDigits
    def input_dg():
        return

    res = input_dg(input)
    print(res)
