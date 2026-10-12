class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # nums in range 1,n contains n+1 integers with ONE repeated integer
        # try to solve without modifying array nums and use o(1) space

        # array problem, do we do slow/fast pointer or two ends pointer
        # instead of using hash set, treat array like a linked List
        # from index i, next index is nums[i], every value is valid index

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break


        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        
