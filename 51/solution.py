from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        grid = []
        for i in range(n):
            grid.append( ['.'] * n )

        return self.solve( grid, [] )[-1]
    
    def solve( self, grid, solutions, row=0 ):
        
        if row >= len(grid):
            return (True, grid, solutions)
        
        for col in range( len(grid) ):

            # We can place a queen at this location                
            if self.is_col_viable( grid, col, row ):

                grid[ row ][ col ] = 'Q'
                valid, grid, solutions = self.solve( grid, solutions, row=row+1 )

                # a valid solution
                if valid:
                    solutions.append( [ ''.join(grid[i]) for i in range(len(grid))   ] )

                # keep going through the possibilities
                grid[row][col] = '.'

        # we got through the column, no valid solutions available
        return (False, grid, solutions)
        

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
        
print (Solution().solveNQueens( 5 ))