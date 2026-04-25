class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # MIN HEAP
        self.queue = []
        self.limit = k

        for num in nums:
            heapq.heappush(self.queue,num)
            if len(self.queue) > self.limit:
                heapq.heappop(self.queue)


    def add(self, val: int) -> int:
        heapq.heappush(self.queue,val)

        if len(self.queue) > self.limit:
            heapq.heappop(self.queue)

        return self.queue[0]
        
