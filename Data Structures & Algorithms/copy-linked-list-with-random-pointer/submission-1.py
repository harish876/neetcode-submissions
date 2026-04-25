"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
            [3,null]

            mp
            3 -> Node(3) [3,null]
            7 -> Node(7) [7,3]
            4 -> Node(4)

        """
        self.head, self.tail = None, None
        mp = {}

        if not head:
            return None

        def insert(curr):
            if self.head == self.tail == None:
                self.head = self.tail = curr 
            
            else:
                self.tail.next = curr
                self.tail = curr

        curr = head
        while curr:
            if curr not in mp:
                nnode = Node(curr.val)
                mp[curr] = nnode
            
            if curr.random and curr.random not in mp:
                nnode = Node(curr.random.val)
                mp[curr.random] = nnode 
            
            if curr.random:
                mp[curr].random = mp[curr.random]

            insert(mp[curr])
            curr = curr.next

        return mp[head]
