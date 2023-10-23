from typing import List
import numpy as np

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        grid = np.full( (n,n), '.' )
        return self.solve( grid )
    
    def solve( self, grid, solutions=[], row=0 ):
        
        print ('calling solve')
        
        if row >= len(grid):
            return (True, grid)
        
        for col in range( len(grid) ):
            print (grid)
            print (row,col)
            # We can place a queen at this location                
            if self.is_col_viable( grid, col, row ):

                grid[ row ][ col ] = 'Q'
                valid, grid = self.solve( grid, row=row+1 )

                # valid solution, keep on going!
                if valid:
                    solutions.append( grid )
                    return (True, grid)

                # not a valid solution, try the next column in this row
                else:
                    print ('DEAD END')
                    print (row, col)
                    grid[row][col] = '.'


        # we got through the column, no valid solutions available
        return (False, grid)
        

    def is_col_viable( self, grid, col, current_row ) -> bool:
        
        for row in range( 0, current_row):
            
            # column
            if grid[row][col] == 'Q':
                return False

            #left diagonal
            left_diag_col = col - current_row + row
            if left_diag_col >= 0:
                if grid[row][left_diag_col] == 'Q':
                    return False
            
            #right diagonal
            right_diag_col = col + current_row - row
            if right_diag_col < len(grid):
                if grid[row][right_diag_col] == 'Q':
                    return False
        
        return True
        
        
        
        
print (Solution().solveNQueens( 6 ))