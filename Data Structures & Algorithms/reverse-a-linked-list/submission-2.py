# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, old_head: Optional[ListNode]) -> Optional[ListNode]:
        self.head, self.tail = None, None

        def insert(val:int) -> None:
            nnode = ListNode(val)

            if self.head == self.tail == None:
                self.head = self.tail = nnode
            
            else:
                self.tail.next = nnode
                self.tail = nnode
        
        def reverse(node: Optional[ListNode]):
            if not node:
                return
            
            reverse(node.next)
            insert(node.val)
        
        reverse(old_head)
        return self.head
