# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
            root -> x does not contain nodes with values greater than x
        """
        result = []

        def helper(curr: TreeNode, maxPathNode: TreeNode):
            if not curr:
                return 0
        
            if curr.val >= maxPathNode.val:
                maxPathNode = curr
                result.append(curr.val)
        
            helper(curr.left, maxPathNode)
            helper(curr.right, maxPathNode)
        
        
        helper(root,root)
        return len(result)