class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
            Straightforward kadane's algorithm

            2  -3   4  -2  2  1  -1   4

            2  -1   4   2  4  5   4   8

        """
        n = len(nums)
        dp = [0 for i in range(n)]
        dp[0], result = nums[0], nums[0]

        for i in range(1,n):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
            result = max(result,dp[i])
        

        return result