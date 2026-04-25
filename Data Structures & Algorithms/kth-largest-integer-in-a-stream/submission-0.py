class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.__k = k
        self.__minHeap = nums
        heapq.heapify(self.__minHeap)
        
        while len(self.__minHeap) > k:
            heapq.heappop(self.__minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.__minHeap,val)

        if len(self.__minHeap) > self.__k:
            heapq.heappop(self.__minHeap)

        return self.__minHeap[0]
        
