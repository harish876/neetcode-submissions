class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
            1. lets do brute force first think through the solution
            2. now lets cache this
            3. now lets do bottom up O(n^2)


        """
        # cache = {}
        # def helper(idx,nums: List[int]) -> bool:
        #     if idx >= len(nums)-1:
        #         return True
            
        #     if idx in cache:
        #         return cache[idx]
            
        #     ans = False
        #     for i in range(1, nums[idx]+1):
        #         ans |= helper(idx + i, nums)

        #     cache[idx] = ans
        #     return ans
        

        # return helper(0,nums)
        n = len(nums)
        dp = [False] * n
        dp[0] = True

        for i in range(1,n):
            for j in range(i):
                if j + nums[j] >= i:
                    dp[i] = True
                    break
        
        ans = True
        for i in dp:
            ans &= i
        
        return ans

