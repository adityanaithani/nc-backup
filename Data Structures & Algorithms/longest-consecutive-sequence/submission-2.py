class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # o(n) time and space
        sequence = set(nums)
        print(sequence)

        longest_streak = 0

        # loop through sequence
        for num in sequence:

            if num - 1 not in sequence:
                current_num = num
                current_streak = 1

                while current_num + 1 in sequence:
                    current_num += 1 
                    current_streak += 1 
                
                longest_streak = max(longest_streak, current_streak)

        return longest_streak