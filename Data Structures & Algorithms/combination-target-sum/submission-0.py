class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        nums = [2 5 6 9]
        target = 9

        with reuse
        """

        path: List[int] = []
        result: List[List[int]] = []

        def findPath(nums: List[int], idx: int, target: int):
            if target < 0 or idx >= len(nums):
                return

            if target == 0:
                result.append(path[:])
                return
            
            
            path.append(nums[idx])
            findPath(nums, idx, target - nums[idx])
            path.pop()

            findPath(nums, idx+1, target)
            
        findPath(nums,0,target)
        return result 
