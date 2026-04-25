class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
            must take b before a
            b -> a

            so no cycles

            we could do top sort or graph coloring

            1 <-> 0
            
        """

        adj = defaultdict(list)
        visited = [0 for _ in range(numCourses)]

        for preq in prerequisites:
            adj[preq[1]].append(preq[0])

        def hasCycle(idx: int, color: int) -> bool: 
            if visited[idx] == 2:
                return True
            
            ans = False
            visited[idx] = 2

            for neighbor in adj[idx]:
                if hasCycle(neighbor, color):
                    return True

            visited[idx] = 1

        
        for i in range(numCourses):
            if visited[i] == 0:    
                if(hasCycle(i,2)):
                    return False
            
        return True
