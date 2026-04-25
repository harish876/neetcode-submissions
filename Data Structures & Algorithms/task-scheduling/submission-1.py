class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
            X X Y Y

            cycle = 0

            identical tasks separated by n CPU Cycles

            n = 2

            X -> Y -> idle -> X -> Y

            A A A B C  (n = 3)


            Max Heap    Heap
                        ze
                 

            get the most done at the starting 
            A -> B -> C -> idle 

        """
        cycle = 0
        minHeap = []
        maxHeap = []

        count = Counter(tasks)
        for key,value in count.items():
            heapq.heappush(maxHeap,(-1 * value, 0))

        while maxHeap or minHeap:
            while minHeap and (cycle >= minHeap[0][0]):
                (time,count) = heapq.heappop(minHeap)
                heapq.heappush(maxHeap,(-1 * count, time))

            
            if not maxHeap:
                cycle = minHeap[0][0]
                continue
            
            (count,time) = heapq.heappop(maxHeap)
            count *= -1
            cycle += 1  
            
            if count > 1:
                heapq.heappush(minHeap,(n+cycle, count-1))
            
            print(maxHeap, minHeap)

            
        return cycle
