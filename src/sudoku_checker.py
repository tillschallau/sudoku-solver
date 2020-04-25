def sudoku_correct(sudoku):
    correct = True
    for row in range(9):
        for col in range(9):
            value = sudoku[row][col]
            print(f"[{row}][{col}] = {value}")
            correct &= check_value(row, col, sudoku, value)
    return correct


def check_value(row, col, sudoku, value):
    for index in range(9):
        if index != col:
            other_val = sudoku[row][index]
            if other_val == value:
                print(f"Value not correct. Row: {row}, Column: {col}, Value: {value}")
                return False
    return True
