class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for point in points:
            x,y = point
            distance = x**2 + y**2
            heapq.heappush(minHeap,(distance,point))
        
        res = []
        while len(minHeap) and k:
            _ , point = heapq.heappop(minHeap)
            res.append(point)
            k-=1
        
        return res