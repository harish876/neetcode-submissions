class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
            lets do brute force first
            think through the solution
        """

        def helper(idx,nums: List[int]) -> bool:
            if idx >= len(nums)-1:
                return True
            
            ans = False
            for i in range(1, nums[idx]+1):
                ans |= helper(idx + i, nums)

            return ans
        

        return helper(0,nums)
