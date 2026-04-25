class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        path: List[int] = []

        def dfs(idx):
            if idx >= len(nums):
                shallowPath = path[:]
                if sorted(shallowPath) not in result:
                    result.append(sorted(shallowPath))

                return

            path.append(nums[idx])
            dfs(idx+1)
            path.pop()

            dfs(idx+1)
            
        dfs(0)
        return result