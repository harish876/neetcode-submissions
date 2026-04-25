class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        2   -1  -1
        0   -1  -1
        1   0   -1

        time = 4
        """

        m, n, queue, result = len(grid), len(grid[0]), deque(), -1
        directions = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]

        fresh_count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_count +=1
                if grid[i][j] == 2:
                    queue.append((i,j))
        
        if len(queue) == 0 and fresh_count == 0:
            return 0
        
        while len(queue):
            sz = len(queue)
            result += 1
            while sz:
                i,j = queue.popleft()
                for (x,y) in directions:
                    nx,ny = i+x, j+y
                    if nx >= 0 and ny >= 0 and nx < m and ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = -1
                        queue.append((nx,ny))
                sz -=1

        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 1):
                    return -1
        
        return result