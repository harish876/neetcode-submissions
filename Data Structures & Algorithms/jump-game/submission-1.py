class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
            1. lets do brute force first think through the solution
            2. now lets cache this


        """
        cache = {}
        def helper(idx,nums: List[int]) -> bool:
            if idx >= len(nums)-1:
                return True
            
            if idx in cache:
                return cache[idx]
            
            ans = False
            for i in range(1, nums[idx]+1):
                ans |= helper(idx + i, nums)

            cache[idx] = ans
            return ans
        

        return helper(0,nums)
