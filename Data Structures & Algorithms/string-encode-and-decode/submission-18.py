class Solution:

    def encode(self, strs: List[str]) -> str:
        """
            Hello World
            5$Hello5$World
        """


        result = ""
        for st in strs:
            result += str(len(st)) + "$" + st
        
        return result


    def decode(self, s: str) -> List[str]:
        result = []
        start, curr, n = 0, 0, len(s)
        print(s)

        while curr < n:
            word_len = ""
            while s[curr] != "$":
                word_len += s[curr]
                curr += 1 

            word_len = int(word_len)

            word_start = curr + 1
            result.append(s[word_start: word_start+word_len])
            curr = curr + word_len + 1


        return result
