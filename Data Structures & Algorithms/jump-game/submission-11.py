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

            Potential optimization would be DP from here right -> O(n^2)
            but greedy would be O(n)

            I would say if there is a true, move the goalpost to that right

            0   1   2   3
            2   5   0   0
            F   T   F   T

        """
        n = len(nums)

        # cache = {}
        # def dfs(idx: int) -> bool:
        #     if idx >= n-1:
        #         return True
            
        #     if idx in cache:
        #         return cache[idx]
            
        #     ans = False

        #     for jump in range(1, nums[idx]+1):
        #         ans |= dfs(idx + jump)

        #     cache[idx] = ans
        #     return ans
        
        # return dfs(0)

        dp = [False] * n
        dp[n-1] = True
        target = n-1

        for i in range(n-2,-1,-1):
            if i + nums[i] >= target:
                dp[i] = True
                target = i
                    
        return dp[0]

