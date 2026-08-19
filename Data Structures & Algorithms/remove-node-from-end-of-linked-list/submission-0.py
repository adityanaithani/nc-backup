# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # set n-1.next to n+1
        # idea is just remove n from the list reference
        # empty edge case on either side
        # either side = use two pointers
        # first pointer moves to head + n
        # second pointer starts BEFORE head, then iterate both until first is null
        # then second is just before removed node, set second.next to two nodes after

        dummy = ListNode(0, head)
        first, second = dummy, head

        while n > 0:
            second = second.next
            n -= 1

        while second: 
            first = first.next
            second = second.next

        first.next = first.next.next

        return dummy.next