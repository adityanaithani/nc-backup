class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find mid
        # if key is mid, return
        # if key is bigger than mid, move mid to right half
        # if key is smaller than mid, move mid to left half

        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            # calculate mid
            mid = lo + (hi - lo) // 2
            # compare mid
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                # lo becomes mid + 1, shrink window to mid+1 -> hi
                lo = mid + 1
            else:
                # hi becomes mid - 1, shrink window to lo -> mid-1
                hi = mid - 1
            
        return -1
