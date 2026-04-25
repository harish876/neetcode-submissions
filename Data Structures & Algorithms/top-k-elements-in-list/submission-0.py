class Solution:
    def topKFrequent(self, nums: List[int], K: int) -> List[int]:
        # top k freq elements, heap - minHeap with size
        """
            1 - 1
            2 - 2
        """

        count = Counter(nums)
        heap = []
        result = []

        for k,v in count.items():
            heapq.heappush(heap,(v,k))
            if len(heap) > K:
                heapq.heappop(heap)
            
        while len(heap) > 0:
            _, k = heapq.heappop(heap)
            result.append(k)
        
        return result