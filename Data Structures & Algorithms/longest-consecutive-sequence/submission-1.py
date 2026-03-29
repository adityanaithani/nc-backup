class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # o(n) time and space

        # turn array into set()
        # for each element in the set check if i-1 exists
        # if yes, move on
        # if no, treat as start of sequence and begin counting/incrementing
        sequence = set(nums)
        print(sequence)

        longest_streak = 0

        # loop through sequence
        for num in sequence:
            current_num = 0
            current_streak = 0
            if num - 1 not in sequence:
                current_num = num
                current_streak += 1

                while current_num + 1 in sequence:
                    current_num += 1 
                    current_streak += 1 
                
                longest_streak = max(longest_streak, current_streak)

        return longest_streak