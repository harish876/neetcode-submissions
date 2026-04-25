class Solution:
    def rob(self, nums: List[int]) -> int:
        def dfs(idx: int, modified_nums: int) -> int: 
            if idx >= len(modified_nums):
                return 0
            
            if idx in cache:
                return cache[idx]
            
            cache[idx] = max(
                modified_nums[idx] + dfs(idx+2,modified_nums),
                dfs(idx+1,modified_nums)
            )

            return cache[idx]
        
        n, ans = len(nums), 0
        if n == 1:
            return nums[0]
        
        cache = {}
        ans = max(ans,dfs(0, nums[0:n-1]))
        
        cache = {}
        ans = max(ans,dfs(0, nums[1:n]))

        return ans

