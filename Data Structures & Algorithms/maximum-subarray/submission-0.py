class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
            kadane's algo
        """
        n = len(nums)
        
        dp = [0] * n
        result = nums[0]
        arr_sum = 0

        for i in range(0,n):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
            result = max(result,dp[i])

        return result