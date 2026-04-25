# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(p_node, q_node) -> bool:
            if not p_node and not q_node:
                return True
            
            if p_node and q_node and p_node.val == q_node.val and isSameTree(p_node.left,q_node.left) and isSameTree(p_node.right,q_node.right):
                return True
            
            return False
        


        def helper(root1,root2) -> bool:
            if not root1:
                return False
            
            ans = False
            
            if isSameTree(root1,root2):
                return True

            ans |= helper(root1.left,root2)
            ans |= helper(root1.right,root2)

            return ans

        return helper(root,subRoot)