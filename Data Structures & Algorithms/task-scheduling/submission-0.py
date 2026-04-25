import heapq
from collections import deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        n = 3
        t = 2

        B - 2
        C - 1

        (3,4),(1,5)

        """
        mp = Counter(tasks)
        maxHeap = []
        dq = deque()
        
        for key,val in mp.items():
            heapq.heappush(maxHeap,-1 * val)

        t = 0
        while maxHeap or dq:
            while dq and dq[0][1] < t:
                key, _ = dq.popleft()
                heapq.heappush(maxHeap,-1 * key)

            if maxHeap:
                top = -1 * heapq.heappop(maxHeap)
                if top-1 > 0:
                    dq.append((top-1,t + n))

            t+=1

        return t
        