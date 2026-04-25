class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """


        
        (36,3)
        (30,2)
        (38,1)
        
        [1,0,0,0,0,0,0]
        """

        n = len(temperatures)
        result = [0 for _ in range(n)]

        stack = []

        for i,t in enumerate(temperatures):
            
            while len(stack) and t > stack[-1][0]:
                _, idx = stack.pop()
                result[idx] = i - idx

            stack.append((t,i))
        
        return result