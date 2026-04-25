class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
            GANG GANG

            X Y Y X

            X - 1
            Y - 2


            k = 1

            A   A   A   B   A   B   B
                l
                                c
            A - 3
            B - 1

            k replacements
        """

        freq = {}
        max_freq_seen = float("-inf")
        left, curr, n = 0, 0, len(s)
        result = 0

        while curr < n:
            curr_window_len = curr - left + 1
            freq[s[curr]] = freq.get(s[curr],0) + 1
            max_freq_seen = max(max_freq_seen, freq[s[curr]])

            while curr_window_len - max_freq_seen > k:
                freq[s[left]] -=1
                left+=1
                curr_window_len-=1

                # We dont need to reset the max_freq_seen here
            
            result = max(result,curr_window_len)
            curr+=1
        
        return result



