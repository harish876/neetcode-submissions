class Solution:
    def dfs(self, grid: List[List[str]],i:int, j:int, m:int, n:int) -> None:
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != '1':
            return
        
        grid[i][j] = 'x'

        self.dfs(grid,i-1,j,m,n)
        self.dfs(grid,i+1,j,m,n)
        self.dfs(grid,i,j-1,m,n)
        self.dfs(grid,i,j+1,m,n)

    def numIslands(self, grid: List[List[str]]) -> int:
        """
            Simple DFS
        """
        m,n = len(grid),len(grid[0])
        result = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.dfs(grid,i,j,m,n)
                    result += 1
        
        return result
        
