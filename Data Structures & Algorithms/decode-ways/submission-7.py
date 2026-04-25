class Solution:
    def numDecodings(self, s: str) -> int:
        """
            A -> 1
            B -> 2
            .
            Z -> 26

            256

        """
        def helper(idx:int):
            if idx >= len(s):
                return 1
            
            ans = 0

            single_digit = int(s[idx])
            if single_digit >= 1 and single_digit <= 9:
                ans += helper(idx+1)

            double_digit = int(s[idx: idx+2])
            if double_digit >= 10 and double_digit <= 26:
                ans += helper(idx+2)
            
            return ans

        result = helper(0)
        return result