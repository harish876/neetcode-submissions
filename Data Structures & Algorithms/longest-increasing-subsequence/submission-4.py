class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
            Easy DP

            9   1   4   2   3   3   7

            1   1   2   2   3   1   4
        """
        n = len(nums)
        dp = [1 for _ in range(n)]

        for i in range(1,n):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        
        return max(dp)



