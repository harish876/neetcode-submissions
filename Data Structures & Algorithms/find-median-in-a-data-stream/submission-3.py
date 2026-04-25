class MedianFinder:

    def __init__(self):
        self.left = [] # maxHeap
        self.right = [] # minHeap
        self.size = 0

    def addNum(self, num: int) -> None:
        if len(self.left) == 0:
            heapq.heappush(self.left, -1 * num)

        elif num > (-1 * self.left[0]):
            heapq.heappush(self.right, num)

        else:
            heapq.heappush(self.left, -1 * num)

        
        if len(self.left) - len(self.right) > 1:
            max_left = -1 * heapq.heappop(self.left)
            heapq.heappush(self.right, max_left)
        
        elif len(self.right) - len(self.left) > 1:
            min_right = heapq.heappop(self.right)
            heapq.heappush(self.left, -1 * min_right)
        
        self.size += 1

        
    def findMedian(self) -> float:
        if self.size % 2 == 1:
            return -1 * self.left[0] if len(self.left) > len(self.right) else self.right[0]

        else:
            return (-1 * self.left[0] + self.right[0]) / 2


        
        