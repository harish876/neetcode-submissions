class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        GANG GANG
        """

        max_profit = 0
        min_price_seen = float("inf")

        for i in range(len(prices)):
            if prices[i] <= min_price_seen:
                min_price_seen = prices[i]
            
            max_profit = max(max_profit, prices[i] - min_price_seen)


        return max_profit