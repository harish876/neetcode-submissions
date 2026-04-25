class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        last idx from position 0

        1   2   0   1   0
                        
        0   1   2   3   4


        simulate -> recursion -> memoization -> 1D DP

        subproblem -> at an index i can I essentially reach that from the start

        idx:  0   1   2   3   4
        vals: 1   2   0   1   0
        dp  : T   T   T   T   
        """
        n = len(nums)
        
        # Caching + Memoization
        # cache = {} 
        # def dfs(idx) -> bool:
        #     if idx >= n-1:
        #         return True
            
        #     if idx in cache:
        #         return cache[idx]

        #     ans = False

        #     for jump in range(1, nums[idx] + 1):
        #         ans |= dfs(idx + jump)

        #     cache[idx] = ans
        #     return cache[idx]
        
        # return dfs(0)


        # DP
        dp = [False for _ in range(n)]
        dp[0] = True

        for i in range(1,n):
            for j in range(i-1,-1,-1):
                if dp[j] and j + nums[j] >= i:
                    dp[i] = True
                    break

        return dp[n-1]
