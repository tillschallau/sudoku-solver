from src.sudoku import Sudoku


def solve(sudoku: Sudoku, row, col):
    if col == 9:
        if row == 8:
            print(sudoku)
            return
        solve(sudoku, row + 1, 0)
        return
    if sudoku.sudoku_finished():
        print(sudoku.sudoku)
        return
    if sudoku.needs_solving(row, col):
        for value in range(1, 10):
            new_sudoku = sudoku.place_value(row, col, value)
            if not new_sudoku.sudoku_has_errors():
                solve(new_sudoku, row, col + 1)
    else:
        solve(sudoku, row, col + 1)
    sudoku.place_value(row, col, 0)
