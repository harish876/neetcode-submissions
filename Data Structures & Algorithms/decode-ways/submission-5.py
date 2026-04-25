class Solution:
    def numDecodings(self, s: str) -> int:
        """
            Decode ways

            1012

            12



        """
        n = len(s)
        def decode(idx: int) -> int:
            if idx >= n:
                return 1

            ans = 0
            if int(s[idx:idx+1]) >= 1 and int(s[idx:idx+1]) <= 9:
                ans += decode(idx+1)

            if int(s[idx: idx+2]) >= 10 and int(s[idx: idx+2]) <= 26:
                ans += decode(idx+2)

            return ans

        return decode(0)