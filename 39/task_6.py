from typing import Callable, List, Tuple, Union


class Matrix:
    def __init__(self, *args) -> None:
        """Matrix.
        args:
            either:
                rows: int, cols: int, fill_value: int|float
            either:
                list2d: list[list[int|float]]"""
        first_arg = args[0]
        if isinstance(first_arg, (list, tuple)):
            self.validate_list2d(first_arg)
            self._matrix: List[List[Union[int, float]]] = (
                first_arg  # type: ignore
            )
        else:
            second_arg = args[1]
            third_arg = args[2]
            self.validate_args(first_arg, second_arg, third_arg)
            self.rows: int = first_arg
            self.cols: int = second_arg
            self.fill_value: Union[int, float] = third_arg
            self._matrix = [
                [self.fill_value for _ in range(self.cols)]
                for _ in range(self.rows)
            ]

    @staticmethod
    def validate_list2d(list2d) -> bool:
        msg = "список должен быть прямоугольным, состоящим из чисел"
        first_row_len = len(list2d[0])
        for row in list2d:
            if len(row) != first_row_len:
                raise TypeError(msg)
        for row in list2d:
            for item in row:
                if not isinstance(item, (int, float)):
                    raise TypeError("значения матрицы должны быть числами")
        return True

    @staticmethod
    def validate_args(rows, cols, fill_value) -> bool:
        msg = (
            "аргументы rows, cols - целые числа;"
            " fill_value - произвольное число"
        )
        for item in (rows, cols):
            if not isinstance(item, int):
                raise TypeError(msg)
        if not isinstance(fill_value, (int, float)):
            raise TypeError(msg)
        return True

    def __getitem__(self, index: Tuple[int, int]) -> Union[int, float]:
        self.validate_index(*index)
        rows, cols = index
        return self._matrix[rows][cols]

    def __setitem__(
        self, index: Tuple[int, int], value: Union[int, float]
    ) -> None:
        self.validate_index(*index)
        self.validate_value(value)
        rows, cols = index
        self._matrix[rows][cols] = value

    def validate_index(self, *args) -> bool:
        if len(args) != 2:
            raise IndexError(
                f"len of index must be: 2. passed len:{len(args)}"
            )
        for arg in args:
            if not isinstance(arg, (int)):
                raise TypeError("index must be integer")
        rows, cols = args
        if not 0 <= rows <= len(self._matrix) or not 0 <= cols <= len(
            self._matrix[0]
        ):
            raise IndexError("недопустимые значения индексов")
        return True

    @staticmethod
    def validate_value(value: Union[int, float]) -> bool:
        if not isinstance(value, (int, float)):
            raise TypeError("значения матрицы должны быть числами")
        return True

    def __add__(self, value: Union["Matrix", int, float]) -> "Matrix":
        if isinstance(value, (int, float)):
            self.validate_value(value)
            return self.func_for_matrix_with_digit(value, self.sum_)
        if isinstance(value, Matrix):
            self.validate_matrix_size(value)
            return self.func_for_two_matrix(value, self.sum_)
        raise ValueError

    def __sub__(self, value: Union["Matrix", int, float]) -> "Matrix":
        if isinstance(value, (int, float)):
            self.validate_value(value)
            return self.func_for_matrix_with_digit(value, self.sub_)
        if isinstance(value, Matrix):
            self.validate_matrix_size(value)
            return self.func_for_two_matrix(value, self.sub_)
        raise ValueError

    def validate_matrix_size(self, add_matrix: "Matrix") -> bool:
        """Validate both, matrix have same size."""
        msg = "операции возможны только с матрицами равных размеров"
        if len(self._matrix) != len(add_matrix._matrix):
            raise ValueError(msg)
        for index in range(len(self._matrix)):
            if len(self._matrix[index]) != len(add_matrix._matrix[index]):
                raise ValueError(msg)
        return True

    def func_for_matrix_with_digit(
        self,
        value: Union[int, float],
        func: Callable[
            [Union[int, float], Union[int, float]], Union[int, float]
        ],
    ) -> "Matrix":
        result = []
        for row in self._matrix:
            cur_row = []
            for i in row:
                cur_row.append(func(i, value))
            result.append(cur_row)
        return Matrix(result)

    def func_for_two_matrix(
        self,
        value: "Matrix",
        func: Callable[
            [Union[int, float], Union[int, float]], Union[int, float]
        ],
    ) -> "Matrix":
        result = []
        for row_index in range(len(self._matrix)):
            cur_row = []
            for i, j in zip(self._matrix[row_index], value._matrix[row_index]):
                cur_row.append(func(i, j))
            result.append(cur_row)
        return Matrix(result)

    @staticmethod
    def sum_(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a + b

    @staticmethod
    def sub_(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a - b
