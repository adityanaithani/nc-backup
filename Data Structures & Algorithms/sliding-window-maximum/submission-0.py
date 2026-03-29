from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # O(nlogn) time, O(n) space

        q = deque()
        ret = []
        l = 0

        for r in range(len(nums)):
            # 1. While the back of the queue has a value SMALLER than current...
            while q and nums[q[-1]] < nums[r]:
            #    Pop from the back! (q.pop())
               q.pop()
            # 2. Add current index 'r' to the back
            q.append(r)
            # 3. If the front index 'q[0]' is out of bounds (less than l)...
            #    Pop from the front! (q.popleft())
            if q[0] < l: 
                q.popleft()
            # 4. If our window has reached size k (r + 1 >= k)...
            if (r + 1) >= k:
            #    Add the value at the front of the queue to our result
                ret.append(nums[q[0]])
            #    And move the left pointer 'l'
                l += 1
        return ret
        
