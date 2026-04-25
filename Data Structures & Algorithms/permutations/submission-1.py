class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        [1,2,3]
        """

        result: List[List[int]] = []
        def dfs(idx: int):
            if idx == len(nums):
                result.append(nums.copy())
                return

            for i in range(idx, len(nums)):
                nums[i], nums[idx] = nums[idx],nums[i]
                dfs(idx+1)
                nums[i], nums[idx] = nums[idx],nums[i]

        dfs(0)
        return result