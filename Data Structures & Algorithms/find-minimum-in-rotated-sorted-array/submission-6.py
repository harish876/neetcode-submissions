class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
            minimum in a rotated sorted array

            idea is to see which half is sorted 

            3   4   5   6   1   2
            |                   |
                    |


            1   2   3   4   5   6
            |                   |
                    |
        """

        n = len(nums)
        left, right = 0, n-1

        while left < right:

            mid = left + (right - left) // 2

            if nums[right] >= nums[mid]:
                right = mid

            else:
                left = mid + 1


        return nums[left] 


