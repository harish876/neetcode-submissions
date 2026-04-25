class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
            Prims, Kruskals MST
        """

        #1. Create the mesh list right

        n = len(points)
        adj = defaultdict(list)

        for i in range(n):
            for j in range(i + 1, n):
                xi,yi = points[i]
                xj,yj = points[j]
                cost = abs(xi - xj) + abs(yi - yj)

                adj[i].append((cost,j)) # from -> [(cost, to)]
                adj[j].append((cost,i))
        
        #2. Pick any starting point
        queue = []
        heapq.heappush(queue,(0, 0)) # (distance , vertex (index))
        visited = set()
        cost = 0

        while queue and len(visited) < n:
            distance, curr_idx = heapq.heappop(queue)
            
            if curr_idx in visited:
                continue

            visited.add(curr_idx)
            cost += distance

            for d,neighbor in adj[curr_idx]:
                if neighbor not in visited:
                    heapq.heappush(queue,(d, neighbor)) # should it be distance + d?

        return cost
