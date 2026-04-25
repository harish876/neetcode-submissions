class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
            minCost

            memoization
            
            DP way
        """

        n = len(cost)
        cache = {}
        
        def dfs(i: int) -> int:
            if i >= n:
                return 0

            if i in cache:
                return cache[i]
            
            cache[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return cache[i]


        return min(dfs(0),dfs(1))
