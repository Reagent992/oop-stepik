from typing import Union


Digits = Union[int, float]


class Box3D:
    """Прямоугольный параллелепипед(брусок)."""

    def __init__(self, width: Digits, height: Digits, depth: Digits):
        self.validate_digits(width, height, depth)
        self.width = width
        self.height = height
        self.depth = depth

    @staticmethod
    def validate_digits(*values) -> bool:
        if all(isinstance(value, (int, float)) for value in values):
            return True
        else:
            raise ValueError("Неверное значение.")

    @staticmethod
    def validate_box3d(*values: "Box3D") -> bool:
        if all(type(value) is Box3D for value in values):
            return True
        else:
            raise ValueError("Неверное значение.")

    def __add__(self, value: "Box3D") -> "Box3D":
        """Сложение двух объектов Box3d."""
        self.validate_box3d(value)
        return Box3D(
            self.width + value.width,
            self.height + value.height,
            self.depth + value.depth,
        )

    def __mul__(self, value: Digits) -> "Box3D":
        """Умножение Box3D на число."""
        self.validate_digits(value)
        return Box3D(
            self.width * value,
            self.height * value,
            self.depth * value,
        )

    def __rmul__(self, value: Digits) -> "Box3D":
        """Обратное умножение."""
        return self * value

    def __sub__(self, value: "Box3D") -> "Box3D":
        """Вычитание двух объектов Box3D."""
        self.validate_box3d(value)
        return Box3D(
            self.width - value.width,
            self.height - value.height,
            self.depth - value.depth,
        )

    def __floordiv__(self, value: Digits) -> "Box3D":
        """Целочисленное деление Box3D на число."""
        self.validate_digits(value)
        return Box3D(
            self.width // value,
            self.height // value,
            self.depth // value,
        )

    def __mod__(self, value: Digits) -> "Box3D":
        """Остаток от деление Box3D на число."""
        self.validate_digits(value)
        return Box3D(
            self.width % value,
            self.height % value,
            self.depth % value,
        )


if __name__ == "__main__":
    box1 = Box3D(1, 2, 3)
    box2 = Box3D(2, 3, 4)

    box3 = box1 + box2
    assert box3.width == 3 and box3.height == 5 and box3.depth == 7

    box4 = box1 * 2
    assert box4.width == 2 and box4.height == 4 and box4.depth == 6

    box5 = 2 * box1
    assert box5.width == 2 and box5.height == 4 and box5.depth == 6

    box6 = box2 - box1
    assert box6.width == 1 and box6.height == 1 and box6.depth == 1

    box7 = box2 // 2
    assert box7.width == 1 and box7.height == 1 and box7.depth == 2

    box8 = box2 % 2
    assert box8.width == 0 and box8.height == 1 and box8.depth == 0
