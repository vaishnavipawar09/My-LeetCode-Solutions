class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # Stack stores indices only
        maxarea = 0
        heights.append(0)  # Add a sentinel value to flush stack at the end

        for i in range(len(heights)):
            # Pop until we find a bar shorter than the current one
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                # Calculate width
                width = i if not stack else i - stack[-1] - 1
                maxarea = max(maxarea, h * width)
            stack.append(i)

        return maxarea

#Time Complexity : O(n)
#Space Complexity : O(n)

'''
MY SOLUTION 
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # Stack stores pairs: (index, height)

        for i, h in enumerate(heights):
            start = i
            # While current height is less than the last height in stack
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # Calculate area with popped height as the smallest bar
                maxArea = max(maxArea, height * (i - index))
                start = index  # Update the start to leftmost index
            stack.append((start, h))  # Push current height with its start index

        # Final check for any remaining heights in stack
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea


#Time Complexity : O(n)
#Space Complexity : O(n)
        '''