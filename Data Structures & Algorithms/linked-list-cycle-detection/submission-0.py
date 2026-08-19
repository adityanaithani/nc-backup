# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # true if cycle exists
        # cycle = >=1 node is revisitable via next
        # o(N) time o(1) space

        # naive: run through list, push nodes to a set
        

        cur = head
        seen = set()

        while cur:
            if cur in seen:
                return True
            seen.add(cur)
            cur = cur.next
        return False