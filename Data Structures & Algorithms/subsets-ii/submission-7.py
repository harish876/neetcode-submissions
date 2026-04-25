class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        path: List[int] = []
        nums.sort()

        def dfs(idx):
            if idx >= len(nums):
                shallowPath = path[:]
                if shallowPath not in result:
                    result.append(shallowPath)
                return

            path.append(nums[idx])
            dfs(idx+1)
            path.pop()

            dfs(idx+1)
            
        dfs(0)
        return result