class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
            Number of **distinct** combinations
        """
        n = len(coins)
        cache = {}

        def dfs(idx:int, curr_amount:int) -> int:
            if curr_amount < 0 or idx >= n:
                return 0
            
            if curr_amount == 0:
                return 1
            

            if (idx,curr_amount) in cache:
                return cache[(idx,curr_amount)]

            ans = 0

            ans += dfs(idx, curr_amount - coins[idx])
            ans += dfs(idx+1, curr_amount)    

            cache[(idx,curr_amount)] = ans
            return cache[(idx,curr_amount)]
        
        result = dfs(0,amount)
        return result
            


