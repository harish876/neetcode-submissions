class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
            BFS to be used again here

            2   1   0
            0   1   1
            0   1   2
        """

        m,n = len(grid),len(grid[0])
        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]

        queue = deque()
        fresh_count = 0

        for i in range(m):
            for j in range(n):                
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh_count += 1
                
        if len(queue) == 0 and fresh_count == 0:
            return 0
        
        result = 0

        while queue:
            sz = len(queue)         

            while sz:
                i,j = queue.popleft()   
                for x,y in directions:
                    if i+x >= 0 and j+y >= 0 and i+x < m and j+y < n and grid[i+x][j+y] == 1:
                        grid[i+x][y+j] = 2
                        queue.append((i+x,j+y))
                sz -= 1
            
            result += 1
        
        for i in range(m):
            for j in range(n):                
                if grid[i][j] == 1:
                    return -1


        return result-1