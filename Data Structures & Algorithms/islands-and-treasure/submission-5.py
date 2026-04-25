class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
            3   -1  0    1
            2    2   1   -1
            1   -1  inf -1
            0   -1  inf inf


            start BFS from 0's

        """
        INT_MAX = 2147483647
        m,n = len(grid),len(grid[0])
        directions = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i,j))
        

        while len(queue):
            sz = len(queue)

            while sz:
                (i,j) = queue.popleft()
                for x,y in directions:
                    nx,ny = i+x, j+y
                    if nx >= 0 and ny >= 0 and nx < m and ny < n and grid[nx][ny] == INT_MAX:
                        grid[nx][ny] =  min(grid[nx][ny],1 + grid[i][j])
                        queue.append((nx,ny))

                sz-=1
