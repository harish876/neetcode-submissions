class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
            n = 3
            ()

            ((()

            ()()()
            ()(())

            valid parantheses contain valid ones

            ((()))

            open/close count

        """

        result: List[str] = []

        def dfs(open_count:int, close_count: int, path: str):
            if open_count == 0 and close_count == 0:
                tmp = path
                result.append(tmp)
                return
            
            if open_count == close_count or open_count > 0:
                dfs(open_count-1, close_count, path + '(')
            

            if open_count < close_count:
                dfs(open_count, close_count-1, path + ')')
            
           
        dfs(n, n, '')
        return result
        

