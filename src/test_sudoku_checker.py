from src.sudoku_checker import sudoku_correct

correct_sudoku = [[9, 5, 7, 6, 1, 3, 2, 8, 4], [4, 8, 3, 2, 5, 7, 1, 9, 6], [6, 1, 2, 8, 4, 9, 5, 3, 7],
                  [1, 7, 8, 3, 6, 4, 9, 5, 2], [5, 2, 4, 9, 7, 1, 3, 6, 8], [3, 6, 9, 5, 2, 8, 7, 4, 1],
                  [8, 4, 5, 7, 9, 2, 6, 1, 3], [2, 9, 1, 4, 3, 6, 8, 7, 5], [7, 3, 6, 1, 8, 5, 4, 2, 9]]

wrong_sudoku = [[9, 5, 7, 6, 1, 3, 2, 8, 4], [4, 8, 3, 2, 5, 7, 1, 9, 6], [6, 1, 2, 8, 4, 9, 5, 3, 7],
                [1, 7, 8, 3, 6, 4, 9, 5, 2], [5, 2, 4, 9, 7, 1, 3, 6, 8], [3, 6, 9, 5, 2, 8, 7, 4, 1],
                [8, 4, 5, 7, 9, 2, 6, 1, 3], [2, 9, 1, 4, 3, 6, 8, 7, 5], [1, 1, 1, 1, 1, 1, 1, 1, 1]]


def test_sudoku_correct():
    assert sudoku_correct(correct_sudoku)


def test_sudoku_wrong():
    assert not sudoku_correct(wrong_sudoku)