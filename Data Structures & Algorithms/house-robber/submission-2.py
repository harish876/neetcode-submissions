class Solution:
    def rob(self, nums: List[int]) -> int:
        """
            1   1   3   3
            |
        """

        n = len(nums)
        cache = {}
        def dfs(idx: int) -> int:
            if idx >= n:
                return 0
            
            if idx in cache:
                return cache[idx]

            cache[idx] = max(
                nums[idx] + dfs(idx + 2),
                dfs(idx + 1)
            )

            return cache[idx]


        return dfs(0)
