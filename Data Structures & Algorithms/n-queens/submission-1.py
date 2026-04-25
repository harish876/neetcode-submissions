class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        row = ['.' for _ in range(n)]
        grid = [row.copy() for _ in range(n)]
        result = []

        def isValid(row, col):
            # Lets check vertically
            r = row-1
            while r >= 0:
                if grid[r][col] == 'Q':
                    return False
                r-=1
            
            # Lets check diagonally upward left
            r,c = row-1,col-1
            while r >= 0 and c>= 0:
                if grid[r][c] == 'Q':
                    return False
                r-=1
                c-=1

            # Lets check diagonally upward right
            r,c = row-1,col+1
            while r >= 0 and c < n:
                if grid[r][c] == 'Q':
                    return False
                r-=1
                c+=1

            return True

        def dfs(row: int):
            if row == n:
                formatted_grid = [''.join(r) for r in grid]
                result.append(formatted_grid)
                return
            
            for col in range(0,n):
                if isValid(row, col):
                    grid[row][col] = 'Q'
                    dfs(row+1)
                    grid[row][col] = '.'
        
        
        dfs(0)
        return result