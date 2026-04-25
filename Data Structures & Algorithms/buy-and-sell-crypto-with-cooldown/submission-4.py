class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            [1  3   4   0   4]


            buy = 1
            sell = 3

            profit = 2

        """
        BUY,SELL = 0, 1
        n = len(prices)
        cache = {}

        def dfs(idx: int, action: int) -> int:
            if idx >= n:
                return 0

            if (idx,action) in cache:
                return cache[(idx,action)]

            ans = 0

            # Action of skipping
            ans = max(ans,  dfs(idx + 1, action))
              
            if action == BUY:
                # Action of buying
                ans = max(ans, -prices[idx] + dfs(idx + 1, SELL))
            
            else:
                # Action of selling
                ans = max(ans, prices[idx] + dfs(idx + 2,BUY))

            cache[(idx,action)] = ans
            return cache[(idx,action)]
        

        result = dfs(0, BUY)
        return result
    
            


            
            


