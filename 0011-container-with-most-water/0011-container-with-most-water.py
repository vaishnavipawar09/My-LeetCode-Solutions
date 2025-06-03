class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1                       #Two pointers , left and right 
        maxarea = 0

        while l < r:                                    #Loops through the array, dont want l and r to overlap
            area = min(height[l], height[r]) * (r - l)  #Calculate min tallest height and width
            maxarea = max(maxarea, area)                #Calculate the max area
            if height[l]< height[r]:                    #If height of left ptr is small than right 
                l += 1                                  #increae the left ptr
            else:
                r -= 1                                  #else decrease the right ptr
        return maxarea

#Time Complexity : O(n)
#Space Complexity: O(1)

"""
#BRUTE FORCE
        res = 0

        for l in range(len(height)):
            for  r in range(l+1, len(height)):
                area = min(height[l], height[r]) * (r -  l)
                res = max(res, area)
        return res

        #Time complexity: O(n^2)
        #Space Complexity: O(1)
        """