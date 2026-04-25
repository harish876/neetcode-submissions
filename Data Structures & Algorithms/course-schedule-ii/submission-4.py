class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
            so if no circle give me the optimal ordering type

            based on indegree outdegree stuff


            topological sort

            indegree calculation
        """

        adj = defaultdict(list)
        result = []
        queue = deque()
        indegree = [0 for _ in range(numCourses)]
        
        for p in prerequisites:
            adj[p[1]].append(p[0])
            indegree[p[0]]+=1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        

        while len(queue):
            sz = len(queue)

            while sz:
                top = queue.popleft()
                result.append(top)

                for n in adj[top]:
                    indegree[n] -= 1
                    if indegree[n] == 0:
                        queue.append(n)

                sz -= 1

        for i in indegree:
            if i != 0:
                return []

        return result 




        
