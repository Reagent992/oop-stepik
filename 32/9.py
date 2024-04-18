from typing import Any, Optional


class InputValues:
    def __init__(self, render: "RenderDigit") -> None:
        self.render = render

    def __call__(self, func) -> Any:
        def wrapper(*args, **kwargs):
            digits = func()
            return [self.render(i) for i in digits.split()]

        return wrapper


class RenderDigit:
    """Преобразование строки в целое число."""

    def __call__(self, attr: Any) -> Optional[int]:
        try:
            return int(attr)
        except ValueError:
            return None


render = RenderDigit()


@InputValues(render)
def input_dg():
    return input()


res = input_dg()
print(res)

if __name__ == "__main__":
    d1 = render("123")  # 123 (целое число)
    assert d1 == 123
    d2 = render("45.54")  # None (не целое число)
    assert d2 is None
    d3 = render("-56")  # -56 (целое число)
    assert d3 == -56
    d4 = render("12fg")  # None (не целое число)
    assert d4 is None
    d5 = render("abc")  # None (не целое число)
    assert d5 is None
