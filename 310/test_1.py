from io import StringIO
import sys
from typing import NamedTuple, Tuple
from unittest import TestCase
import unittest
from unittest.mock import patch
from task_1 import TicTacToe, Cell


class DrawMoves(NamedTuple):
    human: Tuple[Tuple[int, int]]
    computer: Tuple[Tuple[int, int]]


class TestTicTacTie(TestCase):
    def setUp(self):
        # Cell
        self.cell = Cell()
        self.default_cell_value = 0
        self.cell_wrong_values = (-1, 3, 100500, "ab", 0.5)
        # TicTacToe
        self.pole = TicTacToe()
        self.wrong_index = 100500
        self.write_index = 1
        self.write_value = 1
        self.user_input = "1 1"

        self.win_combinations = (
            # Rows
            ((0, 0), (0, 1), (0, 2)),
            ((1, 0), (1, 1), (1, 2)),
            ((2, 0), (2, 1), (2, 2)),
            # Columns
            ((0, 0), (1, 0), (2, 0)),
            ((0, 1), (1, 1), (2, 1)),
            ((0, 2), (1, 2), (2, 2)),
            # Diagonals
            ((0, 0), (1, 1), (2, 2)),
            ((0, 2), (1, 1), (2, 0)),
        )
        self.draw_moves = DrawMoves(
            human=((0, 0), (0, 2), (1, 1), (1, 2), (2, 1)),
            computer=((0, 1), (1, 0), (2, 0), (2, 2)),
        )

    def test_create_cell(self):
        """Cell obj is created with right default attribute value."""
        self.assertEqual(
            self.cell.value,
            self.default_cell_value,
            f"default value of Cell.value must be {self.default_cell_value}",
        )

    def test_cell_validation(self):
        """Cell can not have a wrong value."""
        for wrong_value in self.cell_wrong_values:
            with self.assertRaises(
                (ValueError, TypeError),
                msg=(
                    f"Cell with value: {wrong_value} "
                    "must raise ValueError or TypeError"
                ),
            ):
                self.cell.value = wrong_value

    def test_create_tic_tac_toe(self):
        """TicTacToe obj is created with right attributes."""
        self.assertTrue(hasattr(self.pole, "FREE_CELL"))
        self.assertTrue(hasattr(self.pole, "HUMAN_X"))
        self.assertTrue(hasattr(self.pole, "COMPUTER_O"))
        for row in self.pole:
            for obj in row:
                self.assertEqual(type(obj), Cell)

    def test_tic_tac_toe_accessed_by_index(self):
        self.assertEqual(self.pole[0, 0], self.default_cell_value)

    def test_tic_tac_toe_raises_when_accessed_by_wrong_index(self):
        with self.assertRaises(IndexError):
            self.pole[self.wrong_index, self.wrong_index]

    def test_tic_tac_toe_write_by_index(self):
        self.pole[self.write_index, self.write_index] = self.write_value
        self.assertEqual(
            self.pole[self.write_index, self.write_index], self.write_value
        )

    def test_tic_tac_toe_write_by_wrong_index(self):
        with self.assertRaises(IndexError):
            self.pole[self.wrong_index, self.wrong_index] = self.write_value

    def test_tic_tac_toe_init_method(self):
        for row in self.pole:
            for obj in row:
                obj.value = self.write_value
        self.pole.init()
        for row in self.pole:
            for cell in row:
                self.assertEqual(cell.value, self.default_cell_value)

    def test_tic_tac_toe_show_func(self):
        # Redirect stdout to a StringIO object
        captured_output = StringIO()
        sys.stdout = captured_output
        # Call the function that prints
        self.pole.show()
        # Get the printed output
        printed_output = captured_output.getvalue().strip()
        # Reset sys.stdout
        sys.stdout = sys.__stdout__
        expected_output = "\n".join(
            [" ".join([str(cell) for cell in row]) for row in self.pole]
        )
        # Assert the printed output
        self.assertEqual(
            printed_output,
            expected_output,
            'expected realization of show() as "str(Cell) in 3 row. "',
        )

    def test_tic_tac_toe_human_go_method(self, *args, **kwargs):
        self.assertEqual(
            self.pole[self.write_index, self.write_index], TicTacToe.FREE_CELL
        )
        with patch("builtins.input", return_value=self.user_input):
            self.pole.human_go()
            self.assertEqual(
                self.pole[self.write_index, self.write_index], self.write_value
            )

    def test_tic_tac_toe_computer_go_method(self):
        game_field_values_flat = (i.value for row in self.pole for i in row)
        self.assertFalse(all(game_field_values_flat))
        self.pole.computer_go()
        computer_go_game_field_values_flat = (
            cell.value for row in self.pole for cell in row
        )
        self.assertTrue(any(computer_go_game_field_values_flat))

    def test_tic_tac_toe_is_human_win(self):
        for combination in self.win_combinations:
            for cell_index in combination:
                self.pole[cell_index] = TicTacToe.HUMAN_X
            self.assertTrue(self.pole.is_human_win)

    def test_tic_tac_toe_is_computer_win(self):
        for combination in self.win_combinations:
            for cell_index in combination:
                self.pole[cell_index] = TicTacToe.COMPUTER_O
            self.assertTrue(self.pole.is_computer_win)

    def test_tic_tac_toe_is_draw(self):
        for move in self.draw_moves.human:
            self.pole[move] = TicTacToe.HUMAN_X
        for move in self.draw_moves.computer:
            self.pole[move] = TicTacToe.COMPUTER_O
        self.assertTrue(self.pole.is_draw)


if __name__ == "__main__":
    unittest.main()
