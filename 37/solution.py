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
            self.rows[ i ].load_options()
            self.cols[ i ].load_options()
            self.boxes[ i ].load_options()

    def solve( self ):

        self.load_options()

        while True:
            did_something = False
    
            self.print()
            print ()

            for i in range(9):
                for j in range(9):
                    cell = self.rows[i].cells[j]
                    if len(cell.options) == 1:
                        cell.assign_value( self, cell.options.pop(), i, j )
                        did_something = True

            if not did_something:
                for group in [ self.rows, self.cols, self.boxes ]:
                    for i in range( 9 ):
                        
                        options_counts = {}
                        for cell in group[i].cells:
                            for option in cell.options:
                                if option not in options_counts:
                                    options_counts[option] = 1
                                else:
                                    options_counts[option] += 1

                        # check if any given option is only present in one cell
                        for option in options_counts:
                            if options_counts[option] == 1:
                                did_something = True
                                for cell in group[i].cells:
                                    
                                    # make option the ONLY option
                                    if option in cell.options:
                                        cell.options = { option }
                                        print ('-----------')
                                        print (cell.options)
                                        print ('cell.options')
                                        print (cell.options)
                       

            if not did_something:
                return
    
    def print ( self ):
        for i in range(9):
            print ( ' '.join( str(cell.value) for cell in self.rows[i].cells ))
    
    def export( self ):
        board = []
        for i in range(9):
            board.append( [ str(cell.value) for cell in self.rows[i].cells ] )
        return board
    
class Cell:
    def __init__( self, value ):

        self.options = {}
        self.value = value
        if value == '.':
            self.options = set(range(1, 10))
        else:
            self.value = int(self.value)                

    def remove_option( self, number ):
        if number in self.options:
            self.options.remove( number )

    def assign_value( self, grid, value, i, j ):
        grid.grid[i][j] = str(value)
        grid.rows[i].remove_options( self )
        grid.cols[j].remove_options( self )
        grid.boxes[Grid.get_box( i, j )].remove_options( self )

class Cells:
    def __init__( self ):
        self.cells = []
    
    def remove_options( self, cell ):
        for i in range( 9 ):
            self.cells[i].remove_option( cell.value )
        
    def load_options( self ):
        for i in range(9):
            cell = self.cells[i]
            if cell.value != '.':
                self.remove_options( cell )

    def get_set_options( self ):
        options = {}
        for cell in self.cells:
            options.union( cell.options )
        return options
        
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

