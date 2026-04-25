class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result, n = [], len(nums)
        
        def dfs(idx: int):
            if idx >= n:
                result.append(nums.copy())
                return

            for i in range(idx,n):
                nums[i], nums[idx] = nums[idx], nums[i]
                dfs(idx+1)
                nums[i], nums[idx] = nums[idx], nums[i]
        

        dfs(0)
        return result
