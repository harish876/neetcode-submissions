class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
            Idea is to start at all O's in the border and change them to some character Y

            then replace these Y's with O's and the existing O's with X's (the latter first)
        """

        m,n = len(grid),len(grid[0])

        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]

        def dfs(i:int,j:int):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != 'O':
                return

            grid[i][j] = 'Y'
            for x,y in directions:
                dfs(x+i,y+j)
        

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m-1 or j == n-1 and grid[i][j] == 'O':
                    dfs(i,j)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'O':
                    grid[i][j] = 'X'
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'Y':
                    grid[i][j] = 'O'
        