from src.sudoku_checker import sudoku_correct
from src.sudoku import Sudoku

correct_sudoku = Sudoku([[9, 5, 7, 6, 1, 3, 2, 8, 4], [4, 8, 3, 2, 5, 7, 1, 9, 6], [6, 1, 2, 8, 4, 9, 5, 3, 7],
                         [1, 7, 8, 3, 6, 4, 9, 5, 2], [5, 2, 4, 9, 7, 1, 3, 6, 8], [3, 6, 9, 5, 2, 8, 7, 4, 1],
                         [8, 4, 5, 7, 9, 2, 6, 1, 3], [2, 9, 1, 4, 3, 6, 8, 7, 5], [7, 3, 6, 1, 8, 5, 4, 2, 9]])

wrong_sudoku = Sudoku([[3, 7, 4, 1, 6, 8, 5, 2, 9],
                       [5, 1, 9, 4, 2, 7, 6, 8, 3],
                       [2, 8, 6, 3, 9, 5, 7, 1, 4],
                       [6, 9, 8, 5, 4, 1, 3, 7, 2],
                       [1, 2, 3, 7, 8, 6, 9, 4, 5],
                       [4, 5, 7, 9, 3, 2, 1, 6, 8],
                       [9, 6, 2, 8, 7, 4, 5, 3, 0],
                       [0, 0, 0, 0, 1, 0, 4, 0, 0],
                       [7, 0, 0, 2, 0, 3, 0, 9, 6]])


def test_sudoku_check():
    assert wrong_sudoku.sudoku_has_errors()
    assert correct_sudoku.sudoku_finished()