class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
            Number of Distinct Island Variants here
        """
        m,n = len(grid),len(grid[0])
        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]

        def dfs(i:int, j:int):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != '1':
                return
            
            grid[i][j] = -1
            for x,y in directions:
                dfs(x+i,y+j)

        result = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    result += 1
                    dfs(i,j)

        return result