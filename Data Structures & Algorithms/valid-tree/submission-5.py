class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        parents = [i for i in range(n)]
        ranks = [0 for _ in range(n)]

        def find(i) -> int:
            if parents[i] != i:
                parents[i] = find(parents[i])

            return parents[i]
            
        def union(n1, n2) -> bool:
            """
             0 -> 1
             parents: [0,1,2,3,4]
             ranks:   [0,0,0,0,0]


            """
            parent1 = find(n1) 
            parent2 = find(n2)

            if parent1 == parent2:
                return False

            if ranks[parent1] >= ranks[parent2]:
                parents[parent2] = parent1
                ranks[parent1] +=1

            else:
                parents[parent1] = parent2
                ranks[parent2] +=1
            
            return True
            

        for edge in edges:
            if not union(edge[0],edge[1]):
                return False

        root = find(0)
        return all(find(i) == root for i in range(n))