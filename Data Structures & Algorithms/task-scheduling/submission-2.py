class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
            X   X   Y   Y       (n = 2)


            identical tasks separated by n CPU cycles


            A   A   A   B   C   (n = 3)

            A - 3
            B - 1
            C - 1

            t = 3       
            (4,(A,2))
            
            A -> B -> C

        """
        available, scheduled = [], []
        count = Counter(tasks) # sorted map?
        
        for l,f in count.items():
            heapq.heappush(available, (-1 * f, l))
        
        t = 0
        while len(available) or len(scheduled):
            # print("Current Time: ", t)
            while len(scheduled) and t > scheduled[0][0]:
                top_scheduled = heapq.heappop(scheduled)
                l,f = top_scheduled[1]
                heapq.heappush(available,(-1 * f, l))

    
            if len(available) > 0:
                freq, label = heapq.heappop(available)
                freq *= -1

                if freq - 1 > 0:
                    heapq.heappush(scheduled,(t + n, (label,freq-1)))

            # print(available)
            # print(scheduled)
            # print(" ========== ")
            t += 1

        return t