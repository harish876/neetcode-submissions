class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
            subsequence

            2   20  4   10  3   4   5


            2:  1
            20: 1
            4:  1
            10: 1
            3:  1
            4:  1
            5:  1

        """

        n = len(nums)
        mp = defaultdict(int)
        result = 0

        for num in nums:
            mp[num] = 1

        for k in sorted(mp):
            if k-1 in mp:
                mp[k] += mp[k-1]
            
            result = max(result,mp[k])

        return result