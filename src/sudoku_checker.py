import math


def sudoku_correct(sudoku):
    correct = True
    for row in range(9):
        for col in range(9):
            value = sudoku[row][col]
            correct &= check_value(row, col, sudoku, value)
    return correct


def check_value(row, col, sudoku, value):
    return check_value_row(row, col, sudoku, value) & check_value_column(row, col, sudoku, value) & \
           check_value_square(row, col, sudoku, value)


def check_value_row(row, col, sudoku, value):
    for index in range(9):
        if index != col:
            other_val = sudoku[row][index]
            if other_val == value:
                print(f"Value not correct. Row: {row}, Column: {col}, Value: {value} (Duplicate in row)")
                return False
    return True


def check_value_column(row, col, sudoku, value):
    for index in range(9):
        if index != row:
            other_val = sudoku[index][col]
            if other_val == value:
                print(f"Value not correct. Row: {row}, Column: {col}, Value: {value} (Duplicate in column)")
                return False
    return True


def check_value_square(row, col, sudoku, value):
    x = (math.floor(row / 3)) * 3
    y = (math.floor(col / 3)) * 3
    for r in range(x, x+3):
        for c in range(y, y+3):
            other_val = sudoku[r][c]
            if other_val == value and r != row and c != col:
                print(f"Value not correct. Row: {row}, Column: {col}, Value: {value} (Duplicate in square)")
                return False
    return True

