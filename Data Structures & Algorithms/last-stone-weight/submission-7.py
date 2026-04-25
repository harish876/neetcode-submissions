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
            x = heapq.heappop(queue)
            y = heapq.heappop(queue)

            if y > x:
                heapq.heappush(queue,x - y)
        
        print(queue)
        return -1 * queue[0] if len(queue) else 0


