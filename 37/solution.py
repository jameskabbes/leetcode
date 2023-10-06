from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        board = solve( board )
        print (board)

def solve( grid ):

    """recursively solve the sudoku grid"""

    for i in range(9):
        for j in range(9):
            if grid[i][j] == '.':
                for value in range(1,10):
                    if is_valid( grid, i, j, str(value) ):
                        grid[i][j] = str(value)

                        #if there exists a solution where grid[i][j]=value, return the grid
                        if solve( grid ):
                            return grid

                        #else, backtrack and try the next value in the for loop
                        else:
                            grid[i][j] = '.'

                return False
    return True



def is_valid( grid, row_ind, col_ind, value ) -> bool:

    """
    can i place the value in given grid at row and col?
    """

    box_i_base = 3*(row_ind//3)
    box_j_base = 3*(col_ind//3)

    for k in range(9):
        if grid[row_ind][k] == value:
            return False
        if grid[k][col_ind] == value:
            return False

        box_i = box_i_base + k//3
        box_j = box_j_base + k%3
        if grid[box_i][box_j] == value:
            return False

    return True


board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
board = [
    [".",".","9","7","4","8",".",".","."],
    ["7",".",".",".",".",".",".",".","."],
    [".","2",".","1",".","9",".",".","."],
    [".",".","7",".",".",".","2","4","."],
    [".","6","4",".","1",".","5","9","."],
    [".","9","8",".",".",".","3",".","."],
    [".",".",".","8",".","3",".","2","."],
    [".",".",".",".",".",".",".",".","6"],
    [".",".",".","2","7","5","9",".","."]
]



Solution().solveSudoku( board )

