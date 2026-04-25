class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
            O(m * n)
        """
        m,n = len(grid),len(grid[0])
        directions = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]
        queue = deque()
        fresh_count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_count += 1

                elif grid[i][j] == 2: #if rotten add to queue
                    queue.append((i,j))

        if len(queue) == 0 and fresh_count == 0:
            return 0

        result = 0

        while queue:
            sz = len(queue)
            result += 1
            
            while sz:
                curr_rotten_x, curr_rotten_y = queue.popleft()

                for x,y in directions:
                    new_x,new_y = x + curr_rotten_x, y + curr_rotten_y
                    
                    if new_x >= 0 and new_y >= 0 and new_x < m and new_y < n and grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        queue.append((new_x,new_y))

                sz -= 1


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return result-1
