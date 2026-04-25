class MedianFinder:

    def __init__(self):
        self.leftHeap = [] # max heap
        self.rightHeap = [] # min heap

    def addNum(self, num: int) -> None:
        """
        the top of rightHeap >= top of leftHeap
        """
        if self.rightHeap and num > self.rightHeap[0]:
            heapq.heappush(self.rightHeap, num)
        
        else:
            heapq.heappush(self.leftHeap, -1 * num)

        
        if len(self.rightHeap) > len(self.leftHeap):
            minRight = heapq.heappop(self.rightHeap)
            heapq.heappush(self.leftHeap,-1 * minRight)
        

        elif len(self.leftHeap) > len(self.rightHeap):
            maxLeft = heapq.heappop(self.leftHeap)
            heapq.heappush(self.rightHeap,-1 * maxLeft)
        
    def findMedian(self) -> float:
        print("LEFT: ",self.leftHeap)
        print("RIGHT: ",self.rightHeap)
        print(" ====================== ")

        if len(self.leftHeap) > len(self.rightHeap):
            return -1 * self.leftHeap[0]
        
        elif len(self.rightHeap) > len(self.leftHeap):
            return self.rightHeap[0]
        
        else:
            return (-1 * self.leftHeap[0] + self.rightHeap[0]) / 2 
        