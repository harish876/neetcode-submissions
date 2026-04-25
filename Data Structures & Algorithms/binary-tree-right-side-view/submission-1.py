# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
            right most nodes in traversal
        """

        if not root:
            return []

        result = []
        queue = deque()
        queue.append(root)

        while len(queue):
            currLevelSize = len(queue)
            currLevel = []

            while currLevelSize:
                top = queue.popleft()
                currLevel.append(top.val)

                if top.left:
                    queue.append(top.left)
                
                if top.right:
                    queue.append(top.right)

                currLevelSize -=1
            

            if len(currLevel):
                result.append(currLevel[-1])

        return result