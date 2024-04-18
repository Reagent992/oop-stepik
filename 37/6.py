from typing import Union

digits = Union[int, float]


class Vector:

    def __init__(self, *args: digits) -> None:
        self.args_amount = 1
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError("Wrong arg type passed")
            setattr(self, f"x{self.args_amount}", arg)
            self.args_amount += 1

    def __add__(self, obj: "Vector") -> "Vector":
        """Сложение двух векторов."""
        self.validate_class(obj) and self.validate_len(obj)
        return Vector(
            *[
                getattr(self, f"x{i}") + getattr(obj, f"x{i}")
                for i in range(1, self.args_amount)
            ]
        )

    def __sub__(self, obj: "Vector") -> "Vector":
        self.validate_class(obj) and self.validate_len(obj)
        return Vector(
            *[
                getattr(self, f"x{i}") - getattr(obj, f"x{i}")
                for i in range(1, self.args_amount)
            ]
        )

    def __mul__(self, obj: "Vector") -> "Vector":
        self.validate_class(obj) and self.validate_len(obj)
        return Vector(
            *[
                getattr(self, f"x{i}") * getattr(obj, f"x{i}")
                for i in range(1, self.args_amount)
            ]
        )

    def __iadd__(self, obj: Union[digits, "Vector"]) -> "Vector":
        if isinstance(obj, (int, float)):
            self.validate_digits(obj)
            for i in range(1, self.args_amount):
                setattr(self, f"x{i}", getattr(self, f"x{i}") + obj)
        elif isinstance(obj, Vector):
            self.validate_class(obj) and self.validate_len(obj)
            for i in range(1, self.args_amount):
                setattr(
                    self,
                    f"x{i}",
                    getattr(self, f"x{i}") + getattr(obj, f"x{i}"),
                )
        return self

    def __isub__(self, obj: Union[digits, "Vector"]) -> "Vector":
        if isinstance(obj, (int, float)):
            self.validate_digits(obj)
            for i in range(1, self.args_amount):
                setattr(self, f"x{i}", getattr(self, f"x{i}") - obj)
        elif isinstance(obj, Vector):
            self.validate_class(obj) and self.validate_len(obj)
            for i in range(1, self.args_amount):
                setattr(
                    self,
                    f"x{i}",
                    getattr(self, f"x{i}") - getattr(obj, f"x{i}"),
                )
        return self

    def __eq__(self, obj) -> bool:
        self.validate_class(obj) and self.validate_len(obj)
        return all(
            getattr(self, f"x{i}") == getattr(obj, f"x{i}")
            for i in range(1, self.args_amount)
        )

    def __ne__(self, obj) -> bool:
        self.validate_class(obj) and self.validate_len(obj)
        return any(
            getattr(self, f"x{i}") != getattr(obj, f"x{i}")
            for i in range(1, self.args_amount)
        )

    @staticmethod
    def validate_class(obj: "Vector") -> bool:
        if not isinstance(obj, Vector):
            raise ValueError("Wrong obj passed")
        return True

    def validate_len(self, obj: "Vector") -> bool:
        if self.args_amount != obj.args_amount:
            raise ArithmeticError("размерности векторов не совпадают")
        return True

    @staticmethod
    def validate_digits(obj: digits) -> bool:
        if not isinstance(obj, (int, float)):
            raise ValueError("Передано не числовое значение")
        return True


if __name__ == "__main__":
    # Тестовые данные.
    values = (1, 2, 3, 4, 5, 6, 7, 8)
    vector_1_args = values[0], values[1], values[2]
    vector_1_len = len(vector_1_args)
    vector_1_range = range(1, vector_1_len + 1)
    vector_1 = Vector(*vector_1_args)
    vector_2 = Vector(values[1], values[2], values[3])
    vector_3 = Vector(values[2], values[3], values[4], values[5])

    # Создание объектов.
    for i in vector_1_range:
        assert hasattr(
            vector_1, f"x{i}"
        ), "Вектора создаются без аттрибутов x1, x2, x3 и т.д."

    # Сложение объектов.
    adding_vectors = vector_1 + vector_2
    assert id(vector_1) != id(
        adding_vectors
    ), "При сложение Векторов должен создаваться новый объект."
    for i in vector_1_range:
        assert getattr(adding_vectors, f"x{i}") == getattr(
            vector_1, f"x{i}"
        ) + getattr(vector_2, f"x{i}"), "Неверно работает сложение векторов."
    # Валидация на размерность векторов
    try:
        vector_2 + vector_3
    except ArithmeticError:
        assert True
    else:
        assert False, (
            "Не сгенерировалось исключение: ArithmeticError. "
            "При сложение двух Векторов разной размерности."
        )

    # Вычитание объектов.
    subtraction_vectors = vector_1 - vector_2
    assert id(vector_1) != id(
        subtraction_vectors
    ), "При вычитание Векторов должен создаваться новый объект."
    for i in vector_1_range:
        assert getattr(subtraction_vectors, f"x{i}") == getattr(
            vector_1, f"x{i}"
        ) - getattr(vector_2, f"x{i}"), "Неверно работает вычитание векторов."

    # Валидация на размерность векторов.
    try:
        vector_2 - vector_3
    except ArithmeticError:
        assert True
    else:
        assert False, (
            "Не сгенерировалось исключение: ArithmeticError. "
            "При вычитание двух Векторов разной размерности."
        )

    # Умножение объектов.
    multiplication_vectors = vector_1 * vector_2
    assert id(vector_1) != id(
        multiplication_vectors
    ), "При умножение Векторов должен создаваться новый объект."
    for i in vector_1_range:
        assert getattr(multiplication_vectors, f"x{i}") == getattr(
            vector_1, f"x{i}"
        ) * getattr(vector_2, f"x{i}"), "Неверно работает умножение векторов."
    # Валидация на размерность векторов.
    try:
        vector_2 * vector_3
    except ArithmeticError:
        assert True
    else:
        assert False, (
            "Не сгенерировалось исключение: ArithmeticError. "
            "При умножение двух Векторов разной размерности."
        )

    # Сложение вектора с числом через оператор +=.
    vector_4 = Vector(*vector_1_args)
    add_value = 10
    vector_4 += add_value  # type: ignore
    for i in vector_1_range:
        assert (
            getattr(vector_4, f"x{i}") == vector_1_args[i - 1] + add_value
        ), "Неверно работает сложение вектора с числом через оператор +=."

    # Сложение вектора с вектором через оператор +=.
    vector_5 = Vector(*vector_1_args)
    prev_id = id(vector_5)
    vector_5 += vector_2
    assert (
        id(vector_5) == prev_id
    ), "При сложение объектов через += не должен создаваться новый объект."
    for i in vector_1_range:
        assert getattr(vector_5, f"x{i}") == vector_1_args[i - 1] + getattr(
            vector_2, f"x{i}"
        ), "Неверно работает сложение вектора с вектором через оператор +=."
    # Валидация на размерность векторов.
    try:
        vector_2 += vector_3
    except ArithmeticError:
        assert True
    else:
        assert False, (
            "Не сгенерировалось исключение: ArithmeticError. "
            "При умножение двух Векторов разной размерности."
        )

    # Вычитание вектора с числом через оператор -=.
    vector_6 = Vector(*vector_1_args)
    add_value = 10
    vector_6 -= add_value  # type: ignore
    for i in vector_1_range:
        assert (
            getattr(vector_6, f"x{i}") == vector_1_args[i - 1] - add_value
        ), "Неверно работает вычитание вектора с числом через оператор -=."

    # Вычитание вектора с вектором через оператор -=.
    vector_7 = Vector(*vector_1_args)
    prev_id = id(vector_7)
    vector_7 -= vector_2
    assert (
        id(vector_7) == prev_id
    ), "При вычитание объектов через -= не должен создаваться новый объект."
    for i in vector_1_range:
        assert getattr(vector_7, f"x{i}") == vector_1_args[i - 1] - getattr(
            vector_2, f"x{i}"
        ), "Неверно работает вычитание вектора с вектором через оператор -=."
    # Валидация на размерность векторов.
    try:
        vector_2 -= vector_3
    except ArithmeticError:
        assert True
    else:
        assert False, (
            "Не сгенерировалось исключение: ArithmeticError. "
            "При умножение двух Векторов разной размерности."
        )

    # Проверка, являются ли два вектора равными.
    vector_8 = Vector(*vector_1_args)
    assert vector_1 == vector_8, (
        "Неверно работает Проверка, "
        "являются ли два вектора равными через оператор =="
    )

    # Проверка на разность векторов.
    vector_8 = Vector(*vector_1_args)
    assert vector_2 != vector_8, (
        "Неверно работает Проверка, "
        "являются ли два вектора не равными через оператор !="
    )
