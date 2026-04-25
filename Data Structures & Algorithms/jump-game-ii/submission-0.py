class Solution:
    def jump(self, nums: List[int]) -> int:
        """
            brute force recursion ofc

            min number of jumps

            2   4   1   1   1   1   

        """

        n = len(nums)

        def dfs(idx: int) -> int:
            if idx >= n-1:
                return 0
            
            ans = float("inf")
            for i in range(1,nums[idx]+1):
                ans = min(ans, 1 + dfs(idx + i))

            return ans
        
        result = dfs(0)
        return result





