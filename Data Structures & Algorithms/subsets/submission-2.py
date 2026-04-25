class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
            [1 2 3]
                   |

        """
        path = []
        result: List[List[int]] = []

        def helper(nums: List[int], idx: int):
            if idx >= len(nums):
                result.append(path[:])
                return

            #include 
            path.append(nums[idx])
            helper(nums,idx+1)
            path.pop()
            
            #exclude
            helper(nums,idx+1)
        
        
        helper(nums, 0)
        return result