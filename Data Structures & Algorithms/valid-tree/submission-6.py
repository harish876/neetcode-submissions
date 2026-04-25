class UnionFind:
    def __init__(self, capacity:int):
        self.parents = [i for i in range(capacity)]
        self.ranks = [0 for _ in range(capacity)]
    
    def find(self,node:int) -> int:
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        
        return self.parents[node]
    
    def union(self, node1:int, node2:int) -> bool:
        
        parent1 = self.find(node1)
        parent2 = self.find(node2)

        if parent1 == parent2:
            return False
        

        if self.ranks[parent1] >= self.ranks[parent2]:
            self.parents[parent2] = parent1
            self.ranks[parent1] += 1
        
        else:
            self.parents[parent1] = parent2
            self.ranks[parent2] += 1
        
        return True
    
    @property
    def get_num_connected_components(self):
        for i in range(len(self.parents)):
            self.find(i)
        
        return len(set(self.parents))
    

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
            Valid Tree
                0 - 1 - 4  
                |  /|
                2 - 3

            if there is a cyle in the graph it cannot be a tree right
            Also there should be only 1 parent root to the tree right?
            So the graph has to be 1 connected component

        """
        uf = UnionFind(n)
        for edge in edges:
            if not uf.union(edge[0],edge[1]):
                return False
        
        return uf.get_num_connected_components == 1