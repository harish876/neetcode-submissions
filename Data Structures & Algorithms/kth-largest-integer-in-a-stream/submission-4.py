class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.queue = []
        self.k = k

        for num in nums:
            heapq.heappush(self.queue,num)
            if len(self.queue) > k:
                heapq.heappop(self.queue)

    def add(self, val: int) -> int:
        """
            minHeap by default

            3 5 6 7 8

            k = 3

            6,7,8
        """

        heapq.heappush(self.queue,val)

        if len(self.queue) > self.k:
            heapq.heappop(self.queue)
        

        return self.queue[0] if len(self.queue) > 0 else -1


        
