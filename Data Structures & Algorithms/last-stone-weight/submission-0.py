class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap,-1 * stone)

        while len(maxHeap) >= 2:
            first = -1 * heapq.heappop(maxHeap)
            second = -1 * heapq.heappop(maxHeap)

            if first > second:
                heapq.heappush(maxHeap,second - first)
        
        if len(maxHeap) == 0:
            return 0
        
        return -1 * maxHeap[0]
