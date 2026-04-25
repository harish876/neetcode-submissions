class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        cache = {}

        def dfs(idx: int, curr_amount: int) -> int:
            if curr_amount < 0 or idx >= n:
                return float("inf") 
            
            if curr_amount == 0:
                return 0

            if cache.get((idx,curr_amount),None):
                return cache[(idx,curr_amount)]
            
            cache[(idx,curr_amount)] = min(
                1 + dfs(idx,curr_amount - coins[idx]),
                dfs(idx+1, curr_amount)
            )

            return cache[(idx,curr_amount)]
        

        result = dfs(0,amount)
        return -1 if result == float("inf") else result

