class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
            a   b   c
                    i   
            x   y   z
                j           

            a   b   x   z   c   y
                        |

        """

        n1, n2, n3 = len(s1), len(s2), len(s3)
        cache = {}

        if n1 + n2 != n3:
            return False
        
        def dfs(idx1: int, idx2: int) -> bool:
            if idx1 >= n1 and idx2 >= n2:
                return True
            
            if (idx1,idx2) in cache:
                return cache[(idx1,idx2)]

            ans = False
            
            if idx1 < n1 and s1[idx1] == s3[idx1 + idx2]:
                ans |= dfs(idx1 + 1, idx2)
            
            if idx2 < n2 and s2[idx2] == s3[idx1 + idx2]:
                ans |= dfs(idx1, idx2 + 1)

            cache[(idx1,idx2)] = ans
            return ans

        result = dfs(0,0)
        return result