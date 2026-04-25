class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
            unbounded knapsack??
        """
        n = len(coins)

        cache = {}
        def helper(idx:int, target:int):
            if target < 0 or idx >= n:
                return float("inf")

            if target == 0:
                return 0
            

            if (idx,target) in cache:
                return cache[(idx,target)]

            ans = float("inf")

            ans = min(ans, helper(idx+1,target)) # skip
            ans = min(ans, 1 + helper(idx, target - coins[idx]))  # and include

            cache[(idx,target)] = ans
            return ans   

        cache.clear()
        # result = helper(0,amount)
        # return -1 if result == float("inf") else result

        dp = [[float("inf")] * (amount+1) for _ in range(n+1)]
        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1,n+1):
            for j in range(1,amount+1):
                if j >= coins[i-1]:
                    dp[i][j] = min(dp[i-1][j], 1 + dp[i][j - coins[i-1]])
                else:
                    dp[i][j] = dp[i-1][j]

        result = dp[n][amount]
        return -1 if result == float("inf") else result
            

