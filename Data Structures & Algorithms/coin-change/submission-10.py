class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        # Recursion + memoization
        # cache = {}
        # def dfs(idx: int, curr_amount: int) -> int:
        #     if curr_amount < 0 or idx >= n:
        #         return float("inf") 
            
        #     if curr_amount == 0:
        #         return 0

        #     if cache.get((idx,curr_amount),None):
        #         return cache[(idx,curr_amount)]
            
        #     cache[(idx,curr_amount)] = min(
        #         1 + dfs(idx,curr_amount - coins[idx]),
        #         dfs(idx+1, curr_amount)
        #     )

        #     return cache[(idx,curr_amount)]
        #result = dfs(0,amount)
        #return -1 if result == float("inf") else result


        #DP Approach
        dp = [[float("inf") for _ in range(amount+1)] for _ in range(n+1)]
        dp[0][0] = 0
                
        for i in range(1,n+1):
            for j in range(0,amount+1):
                if j - coins[i-1] >= 0:
                    dp[i][j] = min(1 + dp[i][j - coins[i-1]],dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]

        return -1 if dp[n][amount] == float("inf") else dp[n][amount]


