class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        PAD_MAP = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        """
            [3]   [4]   [5]

        """

        result, n = [], len(digits)
        
        if n == 0:
            return result

        def dfs(idx: int, path: List[str]):
            if idx == n:
                tmp = ''.join(path)
                result.append(tmp)
                return

            for char in PAD_MAP[digits[idx]]:
                path.append(char)
                dfs(idx+1,path)
                path.pop()
        
        dfs(0,[])
        return result