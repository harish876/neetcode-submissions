class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
            m   o   n   k   e   y   s
                                i
            m   o   n   e   y   
                                j

            3 options on word1

            insert, delete, replace

            insert: 

        """
        n1, n2 = len(word1), len(word2)

        def dfs(idx1: int, idx2: int) -> int:
            # base cases
            if idx1 >= n1:
                return (n2 - idx2)
            
            elif idx2 >= n2:
                return (n1 - idx1)


            if word1[idx1] == word2[idx2]:
                return dfs(idx1 + 1, idx2 + 1)
            
            else:
                return min(
                    1 + dfs(idx1 + 1, idx2), #delete
                    1 + dfs(idx1, idx2 + 1), #insert
                    1 + dfs(idx1 + 1, idx2 + 1) # replace
                )
        
        result = dfs(0,0)
        return result
        
