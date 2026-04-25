class Solution:
    def jump(self, nums: List[int]) -> int:
        """
            Minimum number of jumps from start 

            Recursion + Memoization

            DP

            Greedy

            0   1   2   3   4   5
            2   4   1   1   1   1
            1   -   -   -   -   -

        """
        n = len(nums)

        # cache = {}
        # def dfs(idx: int) -> int:
        #     if idx >= n-1:
        #         return 0

        #     if idx in cache:
        #         return cache[idx]
            
        #     ans = float("inf")
        #     for jump in range(1,nums[idx]+1):
        #         ans = min(ans,1 + dfs(idx + jump))
            
        #     cache[idx] = ans
        #     return ans

        # return dfs(0)


        dp = [float("inf") for _ in range(n)]
        dp[0] = 0

        for i in range(1,n):
            for j in range(i-1,-1,-1):
                if j + nums[j] >= i:
                    dp[i] = min(dp[i], 1 + dp[j])
        
        return dp[n-1]
