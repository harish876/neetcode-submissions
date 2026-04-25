class UnionFind:
    def __init__(self, n:int):
        self.parents = [i for i in range(n)]
        self.ranks = [0] * n

    
    def find(self,p:int) -> int:
        if p != self.parents[p]:
            self.parents[p] = self.find(self.parents[p])

        return self.parents[p]

    
    def path_compress(self):
        for i in range(len(self.parents)):
            self.find(i)

    def union(self,p1:int, p2:int):
        r1 = self.find(p1)
        r2 = self.find(p2)

        if r1 == r2:
            return

        if self.ranks[r1] >= self.ranks[r2]:
            self.parents[r2] = r1
            self.ranks[r1] += 1

        elif self.ranks[r1] < self.ranks[r2]:
            self.parents[r1] = r2
            self.ranks[r2] += 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
            Union Find right , pretty straightforward
        """

        uf = UnionFind(n)

        for from_node, to_node in edges:
            uf.union(from_node,to_node)
        
        uf.path_compress()
        return len(set(uf.parents))


