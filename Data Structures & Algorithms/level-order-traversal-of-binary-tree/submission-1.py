# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
            BFS traversal in python
        """

        result = []
        queue = deque()

        if not root:
            return result

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

                currLevelSize -= 1

            result.append(currLevel)

        return result
