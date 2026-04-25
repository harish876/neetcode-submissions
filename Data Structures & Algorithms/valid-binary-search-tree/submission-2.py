# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
            dumb approach -> preorder and check for ascending order
        """
        acc = []
        def preorder(root) -> None:
            if not root:
                return


            preorder(root.left)
            acc.append(root.val)
            preorder(root.right)

        preorder(root)
        return (acc == sorted(acc)) and (len(acc) == len(set(acc)))