class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # heights represents the height of a bar with width 1
        # return area of largest rectangle that can be formed among the bars

        # o(N) time and space

        # want to find largest height:width ratio
        # greedily look for highest bar
        # use monotonic increasing stack so end of stack is highest, then use start/end of stack to calculate area 

        # iterate through heights, if next value is greater than stack[-1] then pop, if not then push
        
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h: 
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea

            