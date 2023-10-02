from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        g = Grid(board)
        g.solve()
        print (board)

class Grid:
    
    def __init__( self, grid ):
        
        self.grid = grid
        self.rows =  [ Cells() for i in range(9) ]
        self.cols =  [ Cells() for i in range(9) ]
        self.boxes = [ Cells() for i in range(9) ]
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                cell = Cell( grid[i][j] )
                box = Grid.get_box( i, j )
                self.rows[ i ].cells.append( cell )
                self.cols[ j ].cells.append( cell )
                self.boxes[ box ].cells.append( cell )
    
    @staticmethod
    def get_box( i, j ):
        return 3*(i//3) + (j//3)
    
    def load_options( self ):
        for i in range( 9 ):
            Cells.update_options( self.rows[ i ].cells )
            Cells.update_options( self.cols[ i ].cells )
            Cells.update_options( self.boxes[ i ].cells )

    def solve( self ):

        self.load_options()

        while True:
            did_something = False

            print ('solving loop')

            for i in range(9):
                for j in range(9):
                    cell = self.rows[i].cells[j]
                    if len(cell.options) == 1:
                        cell.value = cell.options[0]
                        self.grid[i][j] = str(cell.options[0])
                        Cells.remove_options( cell, self.rows[i].cells )
                        Cells.remove_options( cell, self.cols[j].cells )
                        Cells.remove_options( cell, self.boxes[ Grid.get_box(i,j) ].cells )
                        did_something = True

            if not did_something:
                return
    
    def export( self ):
        board = []
        for i in range(9):
            board.append( [ str(cell.value) for cell in self.rows[i].cells ] )
        return board
    
class Cell:
    def __init__( self, value ):

        self.options = []
        self.value = value
        if value == '.':
            self.options = list(range(1, 10))
        else:
            self.value = int(self.value)                

    def remove_option( self, number ):
        if number in self.options:
            self.options.remove( number )

class Cells:
    def __init__( self ):
        self.cells = []
    
    def remove_options( cell, cells ):
        for i in range( 9 ):
            cells[i].remove_option( cell.value )
        
    @staticmethod
    def update_options( cells ):
        for i in range(9):
            cell = cells[i]
            if cell.value != '.':
                Cells.remove_options( cell, cells )

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
board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]

Solution().solveSudoku( board )

