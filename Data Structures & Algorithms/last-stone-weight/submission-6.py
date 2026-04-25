class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
            priority queue

            maxHeap -> weights to be inverted
        """

        queue = []
        for stone in stones:
            heapq.heappush(queue,-1 * stone)
        

        while len(queue) > 1:
            x = -1 * heapq.heappop(queue)
            y = -1 * heapq.heappop(queue)

            if x > y:
                heapq.heappush(queue,y - x)
        
        print(queue)
        return -1 * queue[0] if len(queue) else 0


