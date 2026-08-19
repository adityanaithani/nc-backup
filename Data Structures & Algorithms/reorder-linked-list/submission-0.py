# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # goal: reorder to 0, n-1, 1, n-2, 2, n-3, ...  
        # divide list in half
        # first half is normal
        # second half is reversed
        # divide using fast/slow pointers???

        # solution: use recursion
        # start from back, connect last node to initial node, move in pointers, repeat until pointers meet

        def rec(root: ListNode, cur: ListNode) -> ListNode:
            if not cur:
                return root

            root = rec(root, cur.next)
            if not root:
                return None

            temp = None
            if root == cur or root.next == cur:
                cur.next = None
            else: 
                temp = root.next
                root.next = cur
                cur.next = temp

            return temp

        head = rec(head, head.next)


