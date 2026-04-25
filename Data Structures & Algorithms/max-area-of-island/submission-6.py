class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        m,n = len(grid),len(grid[0])

        directions = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]
        
        def dfs(i:int,j:int) -> int:
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != 1:
                return 0

            grid[i][j] = -1
            return 1 + dfs(i-1,j) + dfs(i+1,j) + dfs(i,j-1) + dfs(i,j+1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    result = max(result,dfs(i,j))


        return result