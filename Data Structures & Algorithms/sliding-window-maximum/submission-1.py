from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # O(nlogn) time, O(n) space

        # double ended queue: stores indices where nums[index] is decreasing
        # before adding a new index, pop all elements from the back (left) that are smaller than that index
        # if front index is no longer in window range, pop
        # maximum will always be at front (left) of the queue, q[0]

        q = deque()
        ret = []
        l = 0

        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
               q.pop()
            q.append(r)
            if q[0] < l: 
                q.popleft()
            if (r + 1) >= k:
                ret.append(nums[q[0]])
                l += 1
        return ret
        
