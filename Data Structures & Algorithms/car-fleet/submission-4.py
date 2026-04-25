class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
            with the information in the problem we can find out the time it takes for each car

            speed = distance / time_taken
            time_taken = distance / speed

            t1 = (10 - 1) / 3 = 3
            t2 = (10 - 4) / 2 = 3

            t1 = (10 - 4) / 2 = 3
            t2 = (10 - 1) / 2 = 4.5
            t3 = (10 - 0) / 1 = 10
            t4 = (10 - 7)  / 1 = 3

            0   4   2
            2   1   3

            4   2   0
            1   3   2

            6   2.6 5

            5
            6

        """

        stack = []
        pairs = [(p,s) for p,s in zip(position,speed)]
        pairs.sort(reverse=True)

        for p,s in pairs:
            time_taken = (target - p) / s 
            stack.append(time_taken)

            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
        
        
        return len(stack)