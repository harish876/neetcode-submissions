class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        last idx from position 0

        1   2   0   1   0
                        
        0   1   2   3   4


        simulate -> recursion -> memoization
        """
        n = len(nums)
        cache = {} 

        def dfs(idx) -> bool:
            if idx >= n-1:
                return True
            
            if idx in cache:
                return cache[idx]

            ans = False

            for jump in range(1, nums[idx] + 1):
                ans |= dfs(idx + jump)

            cache[idx] = ans
            return cache[idx]
        

        return dfs(0)