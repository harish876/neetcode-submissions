class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
            aab

            all possible palindroming substrings

            build palindromes dynamically step by step

            if we reach the end then we good right

            always check the left side is a valid palindrome

            a   a   b   \0
            0   1   2   3
                |

            
        """
        result, n = [], len(s)

        def isPalindrome(s: str) -> bool:
            t = len(s)
            for i in range(t // 2):
                if s[i] != s[t - i - 1]:
                    return False

            return True


        def dfs(idx: int, path: List[str]):
            if idx > n:
                return

            if idx == n:
                tmp = path.copy()
                result.append(tmp)
                return
            
            for i in range(1, n+1):
                substr = s[idx: idx+i]
                if not isPalindrome(substr):
                    continue

                path.append(substr)
                dfs(idx+i, path)
                path.pop()

            return
        
        dfs(0,[])

        return result
        

