class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
            Kadane's algo pretty simple

            2   -3  4   -2  2   1   -1  4
            2   0   0   0   0   0   0   0
        """
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        result = dp[0]

        for i in range(1,n):
            dp[i] = max(nums[i],nums[i] + dp[i-1])
            result = max(result,dp[i])
        
        print(dp)
        return result