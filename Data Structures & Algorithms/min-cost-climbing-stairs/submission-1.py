class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
            minCost
        """

        n = len(cost)

        def dfs(i: int) -> int:
            if i >= n:
                return 0
            
            return cost[i] + min(dfs(i+1), dfs(i+2))


        return min(dfs(0),dfs(1))