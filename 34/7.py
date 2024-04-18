from typing import List, NamedTuple, Tuple


class T(NamedTuple):
    horizontal: int
    vertical: int


Matrix = List[List[float]]


class MaxPooling:

    def __init__(
        self, step: Tuple[int, int] = (2, 2), size: Tuple[int, int] = (2, 2)
    ) -> None:
        """
        Размер сканирующего окна.
        step - шаг смещения окна по горизонтали и вертикали.
        size - размер окна по горизонтали и вертикали.
        """
        self.validate_initial(step, size)
        self.step = T(*step)
        self.size = T(*size)

    def __call__(self, matrix: Matrix) -> Matrix:
        """Проход окном по матрице."""
        self.validate_matrix(matrix)
        vertical_matrix_len = len(matrix)
        horizontal_matrix_len = len(matrix[0])
        result: Matrix = []
        cur_vertical_step = 0
        while (
            cur_vertical_step * self.size.vertical
        ) * self.step.vertical <= vertical_matrix_len:
            cur_horizontal_step = 0
            horizontal_windows = []
            cur_window = []
            for _ in range(self.size.horizontal):
                if (
                    cur_horizontal_step * self.step.horizontal
                    + self.size.horizontal
                    <= horizontal_matrix_len
                ):
                    for v in range(self.size.vertical):
                        cur_window.extend(
                            matrix[cur_vertical_step * self.step.vertical + v][
                                cur_horizontal_step
                                * self.step.horizontal : cur_horizontal_step
                                * self.size.horizontal
                                + self.size.horizontal
                            ]
                        )
                    cur_horizontal_step += 1
                    horizontal_windows.append(max(cur_window))
                    cur_window = []
            result.append(horizontal_windows)
            cur_vertical_step += 1
        return result

    @staticmethod
    def validate_initial(*values: Tuple[int, int]) -> bool:
        """Проверка начальных значений."""
        if all(
            (isinstance(i, int) for i in value if isinstance(value, tuple))
            for value in values
        ):
            return True
        else:
            raise ValueError("Передано неверное значение.")

    @staticmethod
    def validate_matrix(matrix: Matrix) -> bool:
        """Проверка матрицы."""
        matrix_check = isinstance(matrix, list)
        lines_type_check = list()
        lines_content_check = list()
        lines_len = list()
        for line in matrix:
            lines_type_check.append(isinstance(line, list))
            lines_content_check.append(
                all(isinstance(i, (int, float)) for i in line)
            )
            lines_len.append(len(line))
        if all(
            (
                all(i == lines_len[0] for i in lines_len),
                all(lines_type_check),
                all(lines_content_check),
                matrix_check,
            )
        ):
            return True
        else:
            raise ValueError("Неверный формат для первого параметра matrix.")


if __name__ == "__main__":
    import time

    start_time = time.time()

    mp = MaxPooling(step=(2, 2), size=(2, 2))
    res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])
    assert res == [[6, 8], [9, 7]]

    mp = MaxPooling(step=(2, 2), size=(2, 2))
    m1 = [[1, 10, 10], [5, 10, 0], [0, 1, 2]]
    m2 = [[1, 10, 10, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
    res1 = mp(m1)
    res2 = mp(m2)

    assert res1 == [[10]], "неверный результат операции MaxPooling"
    assert res2 == [
        [10, 12],
        [40, 300],
    ], "неверный результат операции MaxPooling"

    mp = MaxPooling(step=(3, 3), size=(2, 2))
    m3 = [[1, 12, 14, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
    res3 = mp(m3)
    assert res3 == [
        [12]
    ], "неверный результат операции при MaxPooling(step=(3, 3), size=(2,2))"

    try:
        res = mp([[1, 2], [3, 4, 5]])
    except ValueError:
        assert True
    else:
        assert (
            False
        ), "некорректно отработала проверка (или она отсутствует) на не прямоугольную матрицу"

    try:
        res = mp([[1, 2], [3, "4"]])
    except ValueError:
        assert True
    else:
        assert (
            False
        ), "некорректно отработала проверка (или она отсутствует) на не числовые значения в матрице"

    mp = MaxPooling(step=(1, 1), size=(5, 5))
    res = mp(
        [
            [5, 0, 88, 2, 7, 65],
            [1, 33, 7, 45, 0, 1],
            [54, 8, 2, 38, 22, 7],
            [73, 23, 6, 1, 15, 0],
            [4, 12, 9, 1, 76, 6],
            [0, 15, 10, 8, 11, 78],
        ]
    )
    assert res == [
        [88, 88],
        [76, 78],
    ], "неверный результат операции MaxPooling(step=(1, 1), size=(5, 5))"
    elapsed_time = time.time() - start_time
    print(f"Время выполнения: {elapsed_time} секунд")
