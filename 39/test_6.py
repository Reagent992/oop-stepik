from unittest import TestCase
from task_6 import Matrix


class TestMatrixInitialization(TestCase):
    def setUp(self) -> None:
        # matrix_2d
        self.matrix_value = 100500
        self.list2d = [[1 for _ in range(4)] for _ in range(3)]
        self.matrix_2d = Matrix(self.list2d)
        # args matrix
        self.rows = 3
        self.cols = 4
        self.fill_value = 10
        self.matrix = Matrix(self.rows, self.cols, self.fill_value)
        self.all_matrix = (self.matrix, self.matrix_2d)
        self.expected_result = [
            [self.fill_value for _ in range(self.cols)]
            for _ in range(self.rows)
        ]
        self.new_fill_value = 20
        self.wrong_values = ("a", list, object)
        self.wrong_args = ((0.5, 0.5, 10), ("a", "b", "c"), (0, 0, "a"))

    def test_matrix_created_with_passed_args(self):
        self.assertEqual(self.matrix.rows, self.rows)
        self.assertEqual(self.matrix.cols, self.cols)
        self.assertEqual(self.matrix.fill_value, self.fill_value)
        self.assertEqual(self.matrix._matrix, self.expected_result)

    def test_matrix_init_type_error(self):
        for args in self.wrong_args:
            with self.assertRaises(TypeError):
                Matrix(*args)

    def test_2dmatrix(self):
        self.assertTrue(hasattr(self.matrix_2d, "_matrix"))
        self.assertEqual(self.matrix_2d._matrix, self.list2d)

    def test_get_first_matrix_element(self):
        self.assertEqual(self.matrix[0, 0], self.fill_value)

    def test_get_index_with_errors(self):
        with self.assertRaises(IndexError):
            self.matrix[-1, -1]
        with self.assertRaises(IndexError):
            self.matrix[100500, 100500]
        with self.assertRaises(TypeError):
            self.matrix["a", "b"]

    def test_matrix_write_value_by_index(self):
        self.matrix[0, 0] = self.new_fill_value
        self.assertEqual(self.matrix[0, 0], self.new_fill_value)

    def test_write_new_value_with_wrong_index(self):
        with self.assertRaises(IndexError):
            self.matrix[-1, -1] = self.new_fill_value
        with self.assertRaises(IndexError):
            self.matrix[100500, 100500] = self.new_fill_value
        with self.assertRaises(TypeError):
            self.matrix["a", "b"] = self.new_fill_value

    def test_new_value_of_matrix_must_be_digits(self):
        for value in self.wrong_values:
            with self.assertRaises(TypeError):
                self.matrix[0, 0] = value

    def test_sum_two_matrix(self):
        sum_of_two_matrix = self.matrix + self.matrix
        self.assertEqual(
            sum_of_two_matrix._matrix,
            [
                [self.fill_value * 2 for _ in range(self.cols)]
                for _ in range(self.rows)
            ],
        )

    def test_sum_matrix_with_digit(self):
        increasing_arg = 10.5
        sum_matrix_with_int = self.matrix + increasing_arg
        self.assertEqual(
            sum_matrix_with_int._matrix,
            [
                [self.fill_value + increasing_arg for _ in range(self.cols)]
                for _ in range(self.rows)
            ],
        )

    def test_subtraction_with_digit(self):
        subtraction_arg = 5
        sum_matrix_with_int = self.matrix - subtraction_arg
        self.assertEqual(
            sum_matrix_with_int._matrix,
            [
                [self.fill_value - subtraction_arg for _ in range(self.cols)]
                for _ in range(self.rows)
            ],
        )

    def test_subtraction_of_matrix(self):
        sub_of_two_matrix = self.matrix - self.matrix
        self.assertEqual(
            sub_of_two_matrix._matrix,
            [
                [self.fill_value - self.fill_value for _ in range(self.cols)]
                for _ in range(self.rows)
            ],
        )
