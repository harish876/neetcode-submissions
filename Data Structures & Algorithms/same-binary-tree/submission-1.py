# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def helper(p_node,q_node) -> bool:
            if not p_node and not q_node:
                return True
            
            if p_node and q_node and p_node.val == q_node.val and helper(p_node.left,q_node.left) and helper(p_node.right,q_node.right):
                return True
            
            return False
        

        return helper(p,q)