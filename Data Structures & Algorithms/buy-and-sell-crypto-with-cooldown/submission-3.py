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
        
        def dfs(idx: int, balance: int, action: int) -> int:
            if idx >= n:
                return balance
            
            # Action sell
            # Profit -> prices[idx]
            # Buy should be deducted from the balance, Sell should add to the balance
            # Maximize progits
            ans = 0

            # Action of skipping
            ans = max(ans,  dfs(idx + 1, balance, action))
              
            if action == BUY:
                # Action of buying
                ans = max(ans,dfs(idx + 1, balance - prices[idx], SELL))
            
            else:
                # Action of selling
                ans = max(ans,dfs(idx + 2, balance + prices[idx], BUY))

            return ans
        

        result = dfs(0, 0, BUY)
        return result
    
            


            
            


