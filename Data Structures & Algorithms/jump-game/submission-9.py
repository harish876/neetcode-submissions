class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
            pretty simple with recursion right?

            there is a greedy way to do this

            build an bool array from the end -> O(n)

            0   1   2   3   4
            1   2   0   1   0
            F   F   F   T   T

                T
        """
        n = len(nums)

        cache = {}
        def dfs(idx: int) -> bool:
            if idx >= n-1:
                return True
            
            if idx in cache:
                return cache[idx]
            
            ans = False

            for jump in range(1, nums[idx]+1):
                ans |= dfs(idx + jump)

            cache[idx] = ans
            return ans
        
        return dfs(0)

