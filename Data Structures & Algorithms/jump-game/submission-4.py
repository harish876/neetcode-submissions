class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        last idx from position 0

        1   2   0   1   0
                        
        0   1   2   3   4


        simulate -> greedy
        """
        n = len(nums)

        def dfs(idx) -> bool:
            if idx >= n-1:
                return True

            
            for jump in range(1, nums[idx] + 1):
                if dfs(idx + jump):
                    return True
            

            return False
        

        return dfs(0)