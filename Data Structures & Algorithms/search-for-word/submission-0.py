class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m,n,k = len(board), len(board[0]), len(word)
        
        def dfs(i:int, j:int, idx: int) -> bool:
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[idx]:
                return False
            
            if idx == k-1:
                return True
            
            ans = False
            tmp = board[i][j]
            board[i][j] = '-'

            ans |= dfs(i+1,j,idx+1)
            ans |= dfs(i-1,j,idx+1)
            ans |= dfs(i,j+1,idx+1)
            ans |= dfs(i,j-1,idx+1)

            board[i][j] = tmp
        
            return ans
        

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True
        
        return False
