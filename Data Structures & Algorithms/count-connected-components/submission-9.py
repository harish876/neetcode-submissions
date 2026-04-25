class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
            Just need distinct parents from the parents array
        """

        parents = [i for i in range(n)]
        ranks = [0 for _ in range(n)]

        def find(i):
            if parents[i] != i:
                parents[i] = find(parents[i])
            
            return parents[i]
        

        def union(n1,n2) -> bool: 
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            if ranks[p1] >= ranks[p2]:
                parents[p2] = p1
                ranks[p1] += 1
            
            else:
                parents[p1] = p2
                ranks[p2] += 1
        
            return True
        

        for edge in edges:
            if not union(edge[0],edge[1]):
                print("oopsie")
        
        for i in range(n):
            parents[i] = find(i)

        return len(set(parents))
    