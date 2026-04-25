class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n+1)]
        self.ranks = [0] * (n+1)
    
    def find(self,p:int):
        if p != self.parents[p]:
            self.parents[p] = self.find(self.parents[p])
        
        return self.parents[p]
    
    def union(self,p1:int, p2:int) -> bool:
        r1 = self.find(p1)
        r2 = self.find(p2)

        if r1 == r2:
            return False
        
        if self.ranks[r1] >= self.ranks[r2]:
            self.parents[r2] = r1
            self.ranks[r1] += 1

        else:
            self.parents[r1] = r2
            self.ranks[r2] += 1
        
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for from_node, to_node in edges:
            if not uf.union(from_node,to_node):
                return [from_node,to_node]
        
        return []