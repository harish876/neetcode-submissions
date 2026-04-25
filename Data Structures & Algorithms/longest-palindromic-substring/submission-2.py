class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
            a   b   a   b   d
                    |
                    l
                    r


            O(n^2) -> generating substrings right then to check palindrome would be O(n) -> O(n^3)
            O(n^2)
        """

        curr, n, max_len, result = 0, len(s), 0, ""

        while curr < n:
            left = curr
            right = curr

            while left >= 0 and right < n and s[left] == s[right]:
                if (right - left + 1) >= max_len:
                    result = s[left:right+1]
                    max_len = right-left+1

                left -= 1
                right += 1 
            
            curr += 1

        curr = 0
        while curr < n:
            left = curr-1
            right = curr

            while left >= 0 and right < n and s[left] == s[right]:
                if (right - left + 1) >= max_len:
                    result = s[left:right+1]
                    max_len = right-left+1

                left -= 1
                right += 1 
            
            curr += 1

        return result
