"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mp = {}
        def helper(node) -> Optional['Node']:
            if not node:
                return None

            if node in mp:
                return mp[node]

            if node not in mp:
                node_copy = Node(node.val) # create a single node with the original value
                mp[node] = node_copy # maintain a mapping of the original node to its copy
            
            for neighbor in node.neighbors:
                mp[node].neighbors.append(helper(neighbor))
            
            return mp[node]

        return helper(node)
        