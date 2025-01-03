# Please write a function named row_correct(sudoku: list, row_no: int), which takes a 
# two-dimensional array representing a sudoku grid, and an integer referring to a single 
# row, as its arguments. Rows are indexed from 0.

# The function should return True or False, depending on whether the row is filled 
# in correctly, that is, whether it contains each of the numbers 1 to 9 at most once.

# sudoku = [
#   [9, 0, 0, 0, 8, 0, 3, 0, 0],
#   [2, 0, 0, 2, 5, 0, 7, 0, 0],
#   [0, 2, 0, 3, 0, 0, 0, 0, 4],
#   [2, 9, 4, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 7, 3, 0, 5, 6, 0],
#   [7, 0, 5, 0, 6, 0, 4, 0, 0],
#   [0, 0, 7, 8, 0, 3, 9, 0, 0],
#   [0, 0, 1, 0, 0, 0, 0, 0, 3],
#   [3, 0, 0, 0, 0, 0, 0, 0, 2]
# ]

# print(row_correct(sudoku, 0))
# print(row_correct(sudoku, 1))
# Sample output
# True
# False
# Write your solution here
def row_correct(sudoku: list, row_no: int)-> bool:
    good_row = True
    counter_number=0
    for sk_number in range(1,10):
        if sudoku[row_no].count(sk_number)>1:
            good_row = False
    return good_row

if __name__ == "__main__":
    sudoku = [
    [9, 7, 6, 0, 8, 4, 3, 2, 1],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    print(row_correct(sudoku, 0))
    print(row_correct(sudoku, 1))