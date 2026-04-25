class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
            GANG GANG

            p   w   w   k   e   w
                    |

            w - 1

            
            z   x   y   z   x   y   z
            0   1   2   3

            z - 1
            x - 1
            y - 2


        """

        freq = {}
        left, curr, n = 0, 0, len(s)
        result = 0

        while curr < n:
            freq[s[curr]] = max(0,freq.get(s[curr],0)) + 1
            result = max(result,curr-left)

            while freq[s[curr]] > 1:
                freq[s[left]]-=1
                left+=1

            
            curr+=1  
        
        result = max(result,curr-left)
        return result