class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
            k closest points

            maxHeap of size k

        """

        queue = []

        for point in points:
            distance = math.sqrt(point[0] ** 2 + point[1] ** 2) 
            heapq.heappush(queue,(-1 * distance,point))

            if len(queue) > k:
                heapq.heappop(queue)
        
        return [point for _,point in queue]