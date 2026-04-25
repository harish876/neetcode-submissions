class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
            Another classic DP Problem

            c   a   t
                        |
            c   r   a   b   t  
                            |
        """

        cache = {}
        def dfs(idx1:int, idx2:int) -> int:
            if idx1 >= len(text1) or idx2 >= len(text2):
                return 0         

            if cache.get((idx1,idx2),None):
                return cache[(idx1,idx2)]

            if text1[idx1] == text2[idx2]:
                cache[(idx1,idx2)] = 1 + dfs(idx1+1,idx2+1)
            
            else:
                cache[(idx1,idx2)] = max(
                    dfs(idx1+1,idx2),
                    dfs(idx1,idx2+1)
                )
            
            return cache[(idx1,idx2)]
        
        return dfs(0,0)


