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
        result = helper(0,amount)
        return -1 if result == float("inf") else result
            

