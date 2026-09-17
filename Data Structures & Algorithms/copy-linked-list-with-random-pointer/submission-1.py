"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# deep copy includes:
# next pointer to new node, corresponding to next pointer of original node
# random pointer to new node corresponding to random pointer of original node
# aim for >= o(n) time/space

# naive: traverse the list and copy each to a new list?

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head is None:
            return None

        l1 = head
        while l1:
            l2 = Node(l1.val)
            l2.next = l1.random
            l1.random = l2
            l1 = l1.next

        new_head = head.random

        l1 = head
        while l1: 
            l2 = l1.random
            l2.random = l2.next.random if l2.next else None
            l1 = l1.next

        l1 = head
        while l1 is not None:
            l2 = l1.random
            l1.random = l2.next
            l2.next = l1.next.random if l1.next else None
            l1 = l1.next

        return new_head






        