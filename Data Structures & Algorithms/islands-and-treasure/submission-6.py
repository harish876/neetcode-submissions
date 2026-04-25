class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
            Idea is BFS right but from the treasure chest instead of the land

        """

        queue = deque()
        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]

        m,n = len(grid),len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i,j))
        
        visited = set()

        while queue:
            i,j = queue.popleft()

            for x,y in directions:
                if i+x >= 0 and j+y >=0 and i+x < m and j+y < n and grid[i+x][y+j] != -1 and (i+x,y+j) not in visited:
                    visited.add((i+x,y+j))
                    grid[i+x][j+y] = min(grid[i+x][y+j], 1 + grid[i][j])
                    queue.append((i+x,y+j))
        
        return