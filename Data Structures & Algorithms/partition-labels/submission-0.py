class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
            each letter appears at most one substring

            7 distinct characters

            x   y   x   x   y   z   b   z   b   b   i   s   l
                            |
                            |

            use up all x's and z's


            [in short ensure for any substring there are no character in the curr substring that occur outside]


            current_window_chars = {
                x
                y
                
            }
            
            
            x - 0
            b - 3
            y - 0
            z - 2
            i - 1
            s - 1
            l - 1



        """
        count = Counter(s)
        left, curr, n = 0, 0, len(s)
        current_window_chars, result = set(), []

        while curr < n:
            count[s[curr]] -= 1 
            current_window_chars.add(s[curr])

            tmp = 0
            for seen_char in current_window_chars:
                if count[seen_char] == 0:
                    tmp += 1
        
            if tmp == len(current_window_chars):
                result.append(curr-left+1)
                left = curr+1
                current_window_chars = set()

            curr += 1

        return result