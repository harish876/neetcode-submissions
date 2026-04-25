class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp,result = [0 for _ in range(n)], float("-inf")
        dp[0] = nums[0]
        result = max(result,dp[0])

        for i in range(1, n):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
            result = max(result,dp[i])
        
        return result
