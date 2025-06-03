class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1                       #Two pointers , left and right 
        maxarea = 0

        while l < r:                                    #Loops through the array
            area = min(height[l], height[r]) * (r - l)  #Calculate min tallest height and width
            maxarea = max(maxarea, area)                #Calculate the max area
            if height[l]< height[r]:                    #If height of left ptr is small than right 
                l += 1                                  #increae the left ptr
            else:
                r -= 1                                  #else decrease the right ptr
        return maxarea
