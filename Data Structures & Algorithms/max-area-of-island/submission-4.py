class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
            Same Pattern
        """

        m,n,result = len(grid),len(grid[0]),0

        curr_count = 0

        def dfs(i,j):
            nonlocal curr_count
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != 1:
                return
            
            curr_count +=1
            grid[i][j] = -1

            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)   

        for i in range(m):
            for j in range(n):

                if grid[i][j] == 1:
                    curr_count = 0
                    dfs(i,j)
                    result = max(result,curr_count)
        

        return result

