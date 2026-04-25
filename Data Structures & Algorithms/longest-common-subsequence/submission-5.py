class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
            Another classic DP Problem

            c   a   t
                        |
            c   r   a   b   t  
                            |
        """

        # Recursive + Memoization
        # cache = {}
        # def dfs(idx1:int, idx2:int) -> int:
        #     if idx1 >= len(text1) or idx2 >= len(text2):
        #         return 0         

        #     if cache.get((idx1,idx2),None):
        #         return cache[(idx1,idx2)]

        #     if text1[idx1] == text2[idx2]:
        #         cache[(idx1,idx2)] = 1 + dfs(idx1+1,idx2+1)
            
        #     else:
        #         cache[(idx1,idx2)] = max(
        #             dfs(idx1+1,idx2),
        #             dfs(idx1,idx2+1)
        #         )
            
        #     return cache[(idx1,idx2)]
        
        # return dfs(0,0)
        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]



