class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # return indices i and j such that i+j is target and i neq j
        # naive: n^2 double for loop, start on first index and try all other values
        for i in range (len(nums)):
            for j in range (i + 1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
        return []