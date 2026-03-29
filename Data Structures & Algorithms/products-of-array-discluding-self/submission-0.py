class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        before = []
        beforeTemp = 1
        after = []
        afterTemp = 1
        for i in range(0, len(nums)):
            before.append(beforeTemp)
            beforeTemp *= nums[i]
        for j in range (len(nums) - 1, -1, -1):
            after.append(afterTemp)
            afterTemp *= nums[j]
        after.reverse()
        for k in range(len(nums)):
            # multiply before[i] with after[k]
            output.append(before[k] * after[k]) 
            # append to output[i]
        return output
    