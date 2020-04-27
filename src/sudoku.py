import math
import copy


class Sudoku:
    sudoku = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    starting_sudoku = [[1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    current_row = 0
    current_col = 0

    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.starting_sudoku = copy.deepcopy(sudoku)
        for row in range(9):
            for col in range(9):
                if sudoku[row][col] == 0:
                    current_row = row
                    current_col = col

    def get_current_value(self):
        return self.sudoku[self.current_row][self.current_col]

    def sudoku_has_errors(self):
        correct = True
        for row in range(9):
            for col in range(9):
                value = self.sudoku[row][col]
                correct &= self.check_value(row, col, value, True)
        return not correct

    def sudoku_finished(self):
        correct = True
        for row in range(9):
            for col in range(9):
                value = self.sudoku[row][col]
                correct &= self.check_value(row, col, value)
                correct &= self.sudoku[row][col] != 0
        return correct

    def check_value(self, row, col, value, ignore_zero=False):
        return self.check_value_row(row, col, value, ignore_zero) & self.check_value_column(row, col, value, ignore_zero) & \
               self.check_value_square(row, col, value, ignore_zero)

    def check_value_row(self, row, col, value, ignore_zero=False):
        if not (ignore_zero and value == 0):
            for index in range(9):
                if index != col:
                    other_val = self.sudoku[row][index]
                    if other_val == value:
                        # print(f"Value not correct. Row: {row}, Column: {col}, Value: {value} (Duplicate in row)")
                        return False
        return True

    def check_value_column(self, row, col, value, ignore_zero=False):
        if not (ignore_zero and value == 0):
            for index in range(9):
                if index != row:
                    other_val = self.sudoku[index][col]
                    if other_val == value:
                        # print(f"Value not correct. Row: {row}, Column: {col}, Value: {value} (Duplicate in column)")
                        return False
        return True

    def check_value_square(self, row, col, value, ignore_zero=False):
        if not (ignore_zero and value == 0):
            x = (math.floor(row / 3)) * 3
            y = (math.floor(col / 3)) * 3
            for r in range(x, x + 3):
                for c in range(y, y + 3):
                    other_val = self.sudoku[r][c]
                    if other_val == value and r != row and c != col:
                        # print(f"Value not correct. Row: {row}, Column: {col}, Value: {value} (Duplicate in square)")
                        return False
        return True

    def needs_solving(self, row, col):
        return self.starting_sudoku[row][col] == 0

    def place_value(self, row, col, value):
        if self.needs_solving(row, col):
            self.sudoku[row][col] = value
        return self
