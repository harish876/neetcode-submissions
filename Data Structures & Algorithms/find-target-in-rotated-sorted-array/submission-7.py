class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """

            1   2   3   4   5   6
                    |

            3   4   5   6   1   2  
                                r
                            m
                        l
            
            
            5   1   3
            l
                    r
                m
            
            target = 3
        """

        left, right = 0, len(nums)-1

        while left <= right:

            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            

            elif nums[mid] >= nums[left]:
                if nums[mid] >= target and target >= nums[left]:
                    right = mid - 1
                
                else:
                    left = mid + 1
            
            else:
                if target >= nums[mid] and nums[right] >= target:
                    left = mid + 1
                
                else:
                    right = mid - 1
        
        return -1