class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # o(n) time o(1) space

        # area is height times distance
        # so that is the smallest of the two heights
        # times the distance between the two indices

        # naive, two pointers, start from opposite ends
        # take first two bars, calculate area

        i = 0
        j = len(heights) - 1
        max_area = 0

        while i < j:
            print(i,j)
            l = min(heights[i], heights[j])
            w = j - i
            print(l,w)
            max_area = max(max_area, l*w)
            # increment pointers
            if heights[i] > heights[j]:
                j -= 1
            elif heights[i] < heights[j]:
                i += 1
            else: 
                j -= 1
                i += 1
            print(max_area)
        return max_area
