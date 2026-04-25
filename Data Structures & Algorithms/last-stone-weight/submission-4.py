class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """

        """
        queue = [] # MAX HEAP
        for stone in stones:
            heapq.heappush(queue, -1 * stone)
        

        while queue:
            if len(queue) == 1:
                return -1 * queue[0]
            
            first = -1 * heapq.heappop(queue)
            second = -1 * heapq.heappop(queue)

            if first == second:
                continue
            
            elif first < second:
                heapq.heappush(queue, first-second)
            
            else:
                heapq.heappush(queue, second-first)
            

        return 0