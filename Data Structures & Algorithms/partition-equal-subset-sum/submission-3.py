class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
            Very Good DP Problem

            1   2   3   4

            5

            this now becomes a coin change problem -> bounded knapsack
        """

        n,num_sum = len(nums),sum(nums)

        if num_sum % 2 == 1:
            return False
        
        target = num_sum // 2
        
        dp = [[False for _ in range(target+1)] for _ in range(n+1)]
        dp[0][0] = True

        for i in range(1,n+1):
            for j in range(target+1):
                if j - nums[i-1] >= 0:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i-1]]
                
                else:
                    dp[i][j] |= dp[i-1][j]
        
        return dp[n][target]



