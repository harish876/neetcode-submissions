class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n, result, prev_max, prev_min = len(nums), nums[0], nums[0], nums[0]

        for i in range(1,n):
            num = nums[i]
            curr_max = max(num, num * prev_max, num * prev_min)
            curr_min = min(num, num * prev_max, num * prev_min)

            prev_max = curr_max
            prev_min = curr_min

            result = max(result,curr_max)
        
        return result