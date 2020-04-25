from array import *
from numpy import random


def sudoku_correct(sudoku):
    correct = True
    for row in range(8):
        for col in range(8):
            value = sudoku[row][col]
            correct &= check_value(row, col, sudoku, value)
    return correct


def check_value(row, col, sudoku, value):
    for index in range(8):
        if index != col:
            other_val = sudoku[row][index]
            if other_val == value:
                print(f"Value not correct. Row: {row}, Column: {col}, Value: {value}")
                return False
    return True


T = random.choice(list(range(0, 9)), size=(9, 9))

print(T)

print(f"Correct? {sudoku_correct(T)}")
