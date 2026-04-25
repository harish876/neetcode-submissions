class UnionFind:
    def __init__(self, capacity:int):
        self.parents = [i for i in range(capacity)]
        self.ranks = [0 for _ in range(capacity)]
    

    def find(self,node: int) -> int:
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        
        return self.parents[node]
    

    def union(self,node1:int, node2:int) -> bool:
        parent1 = self.find(node1)
        parent2 = self.find(node2)

        if parent1 == parent2:
            return False # this is a cycle right
        
        if self.ranks[parent1] >= self.ranks[parent2]:
            self.parents[parent2] = parent1
            self.ranks[parent1] += 1
        
        else:
            self.parents[parent1] = parent2
            self.ranks[parent2] += 1

        return True

    @property
    def get_num_connected_components(self) -> int:
        for i in range(len(self.parents)):
            self.find(i)

        return len(set(self.parents))

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
            0 -> 1 -> 2 -> 3
        """
        uf = UnionFind(n)

        for from_node,to_node in edges:
            uf.union(from_node,to_node) # This should be always true, else it indicates a cycle right -> should not happen
        
        return uf.get_num_connected_components