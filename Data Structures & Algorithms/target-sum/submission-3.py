class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
            total number of ways to find sum
        """

        n = len(nums)
        cache = {}

        def dfs(idx: int, curr_target: int) -> int:
            if idx >= n:
                if curr_target == target:
                    return 1
                else:
                    return 0
            
            if (idx,curr_target) in cache:
                return cache[(idx,curr_target)]
            
            ans = 0

            ans += dfs(idx+1, curr_target + nums[idx])
            ans += dfs(idx+1, curr_target - nums[idx])

            cache[(idx,curr_target)] = ans
            return ans
        

        return dfs(0,0)
            

