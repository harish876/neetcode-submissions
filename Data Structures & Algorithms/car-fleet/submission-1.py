class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        [4, 1, 0, 7]
        [2, 2, 1, 1]

        position and speed tuples and sorting

        [(7, 1), (4, 2), (1, 2), (0, 1)]


        9
        4.5
        3
        """

        n = len(position)
        tuple_list = [(position[i],speed[i]) for i in range(n)]
        tuple_list = sorted(tuple_list,reverse = True)
        print(tuple_list)

        stack = []
        for position,speed in tuple_list:
            time = (target - position) / speed

            while len(stack) and time <= stack[-1]:
                slow_time = stack.pop()
                time = slow_time

            stack.append(time)

        return len(stack)