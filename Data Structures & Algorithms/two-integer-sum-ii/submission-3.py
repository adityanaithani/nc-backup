class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # sorted in non-decreasing order
        # two numbers add up to target and idx1 < idx2, also not equal
        l = 0
        r = len(numbers) - 1

        while l < len(numbers):
            current_sum = numbers[l] + numbers[r]
            if current_sum > target:
                r -= 1
            elif current_sum < target:
                l += 1
            else:
                return [l + 1, r + 1]
