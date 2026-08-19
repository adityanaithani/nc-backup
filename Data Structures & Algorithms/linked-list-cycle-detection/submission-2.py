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

        # naive: run through list, use a seen set(), return true if the next element is in the set

        # slow/fast pointers: if cycle, fast will lap slow
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
            