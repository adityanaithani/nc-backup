class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output = []
        # before = []
        # beforeTemp = 1
        # after = []
        # afterTemp = 1
        # for i in range(0, len(nums)):
        #     before.append(beforeTemp)
        #     beforeTemp *= nums[i]
        # for j in range (len(nums) - 1, -1, -1):
        #     after.append(afterTemp)
        #     afterTemp *= nums[j]
        # after.reverse()
        # for k in range(len(nums)):
        #     output.append(before[k] * after[k]) 
        # return output

        # in-place solution:
        # build output array during first loop (i), store values directly in output
        # run after (j) loop on the same array, multiplying the temp value with the value already in output[i] and updating it then

        output = []
        beforeTemp = 1
        afterTemp = 1
        for i in range(0, len(nums)):
            output.append(beforeTemp)
            beforeTemp *= nums [i]
        for j in range (len(nums) - 1, -1, -1):
            output[j] *= afterTemp
            afterTemp *= nums[j]
        return output