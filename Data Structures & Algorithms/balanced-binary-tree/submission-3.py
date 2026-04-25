# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
                1
              n    2
                  n  3

        """
        def height(root) -> int:
            if not root:
                return 0
            
            return 1 + max(height(root.left),height(root.right))


        def dfs(root) -> bool:
            if not root:
                return True

            left_h, right_h = height(root.left), height(root.right)

            if abs(left_h - right_h) <= 1 and dfs(root.left) and dfs(root.right):
                return True
            
            return False
        

        return dfs(root)