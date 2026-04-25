class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
            GANG GANG


            l   e   c   a   b   e   e   e
                    |       |
        """

        # Fixed size sliding window

        window_size = len(s1)
        left, curr, n = 0, 0, len(s2)
        actual, expected = {}, Counter(s1)

        # print("Check equality of maps: ", {'a': 2, 'b': 2} == {'b': 2, 'a': 1})

        while curr < n:
            actual[s2[curr]] = actual.get(s2[curr],0) + 1

            if (curr-left+1) == window_size:
                if actual == expected:
                    return True
                
                actual[s2[left]] -= 1
                if actual[s2[left]] <= 0:
                    del actual[s2[left]]
                
                left+=1

            curr +=1
        
        return False