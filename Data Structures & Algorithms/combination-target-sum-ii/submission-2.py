class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        """
            findPath

            without reuse

          idx
            1   2   2   3   4   5
            |


            9   2   2   4   6   1   5
                    |

        """

        path = []
        result = []
        nums.sort()

        def findPath(idx: int , target: int):            
            if target == 0:
                result.append(path[:])
                return

            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue

                if target - nums[i] < 0:
                    break
                
                path.append(nums[i])
                findPath(i+1,target - nums[i])
                path.pop()
                    
        findPath(0, target)
        return result