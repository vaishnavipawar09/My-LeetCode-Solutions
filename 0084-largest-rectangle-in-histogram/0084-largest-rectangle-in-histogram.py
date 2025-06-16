class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0
        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                maxarea = max(maxarea, h * width)
            stack.append(i)
        return maxarea

#Time Complexity : O(n)
#Space Complexity : O(n)
        