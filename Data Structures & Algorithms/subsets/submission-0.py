class Solution:    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
            1 2 3
        """
        ans = []
        def backtrack(curr: int, acc: List[int]):
            if curr >= len(nums):
                ans.append(acc[:])
                return
            

            acc.append(nums[curr])
            backtrack(curr+1,acc)
            acc.pop()

            backtrack(curr+1,acc)

        backtrack(0,[])
        return ans