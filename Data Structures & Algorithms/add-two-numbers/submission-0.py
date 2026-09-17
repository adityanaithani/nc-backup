# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#   while head is not None:
#         print(head.data, end="")
#         if head.next is not None:   
#             print(" -> ", end="")
#         head = head.next
#     print()



#         if head is None:
#             return None

#         l1 = head
#         while l1:
#             l2 = Node(l1.val)
#             l2.next = l1.random
#             l1.random = l2
#             l1 = l1.next

            
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # traverse each list, add each value into variables, reverse, then add
        # o(m + n) time and o(1) space
        # new_number = (number * 10) + digit

        final_list = ListNode()
        current_pointer = final_list
        
        carry_number = 0
        while l1 or l2 or carry_number:
            value_1 = l1.val if l1 else 0
            value_2 = l2.val if l2 else 0

            new_digit_value = value_1 + value_2 + carry_number
            carry_number = new_digit_value // 10
            new_digit_value = new_digit_value % 10
            current_pointer.next = ListNode(new_digit_value)

            current_pointer = current_pointer.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return final_list.next
