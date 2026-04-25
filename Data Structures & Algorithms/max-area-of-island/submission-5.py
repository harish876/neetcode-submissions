class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
            same logic, compute area in a single pass
        """
        m,n = len(grid), len(grid[0])

        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]

        self.ans = 0

        def dfs(i:int, j:int):

            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != 1:
                return 0
                

            grid[i][j] = -1
            self.ans += 1
            
            for x,y in directions:
                dfs(x+i,y+j)
            
                
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.ans = 0
                    dfs(i,j)
                    result = max(result,self.ans)
        
        return result