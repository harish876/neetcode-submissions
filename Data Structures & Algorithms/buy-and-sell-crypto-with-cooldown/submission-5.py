class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            1   3   4   0   4
                            |
            B           B   S

            profit = 2 + 4 = 6

            current_state

            0 -> buy (if prev_state == 0 then lets buy)
            1 -> sell (if prev_state == 1 then sell it, we will advance the pointer by +2)
        """
        n = len(prices)

        cache = {}
        def helper(idx:int, curr_state: int):
            if idx >= n:
                return 0
            
            if (idx,curr_state) in cache:
                return cache[(idx,curr_state)]
            
            ans = 0
            
            ans = max(ans,helper(idx+1, curr_state)) # no op

            if curr_state == 0:
                ans = max(ans, -prices[idx] + helper(idx+1, 1))
            
            else:
                ans = max(ans, prices[idx] + helper(idx+2, 0))

            cache[(idx,curr_state)] = ans
            return ans
        
        cache.clear()
        result = helper(0, 0)
        return result


