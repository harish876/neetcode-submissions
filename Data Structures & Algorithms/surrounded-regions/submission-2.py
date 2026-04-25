class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        [
            ["X","X","X","X"],
            ["X","O","O","X"],
            ["X","O","O","X"],
            ["X","X","X","O"]
        ]

        BFS or maybe DFS starting from all O's
        """

        m, n = len(board), len(board[0])
        
        def isBorder(i,j) -> bool:
            return i == 0 or j == 0 or i == m-1 or j == n-1
        
        def dfs(i,j):
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != 'O':
                return 
            
            board[i][j] = '-'

            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        

        for i in range(m):
            for j in range(n):
                if isBorder(i,j) and board[i][j] == 'O':
                    dfs(i,j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                
                elif board[i][j] == '-':
                    board[i][j] = 'O'

