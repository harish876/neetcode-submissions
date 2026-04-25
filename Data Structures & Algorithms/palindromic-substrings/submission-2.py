class Solution:
    def countSubstrings(self, s: str) -> int:
        """

            substrings -> O(n^2)
            checking palindrome -> O(n)


            aaa
            
        """

        curr, n, result = 0, len(s), 0

        # Odd Length
        while curr < n:
            left = curr
            right = curr

            while left >= 0 and right < n and s[left] == s[right]:
                result += 1
                left -=1
                right +=1
            

            curr += 1

        # Even Length
        curr = 0
        while curr < n:
            left = curr-1
            right = curr

            while left >= 0 and right < n and s[left] == s[right]:
                result += 1
                left -=1
                right +=1
            
            curr += 1

        return result