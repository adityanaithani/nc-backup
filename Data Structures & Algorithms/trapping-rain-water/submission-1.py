class Solution:
    def trap(self, height: List[int]) -> int:
        # o(n) or better time/space
        # container with most water on steroids
        # two pointers again (?) starting on either end

        # water at i = min(left_max, right_max) - height[i]
        if not height:
            return 0
        
        l = 0
        r = len(height) - 1
        lmax = height[l]
        rmax = height[r]
        amount = 0

        while l < r: 
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                amount += lmax - height[l]
            else: 
                r -= 1
                rmax = max(rmax, height[r])
                amount += rmax - height[r]
        return amount