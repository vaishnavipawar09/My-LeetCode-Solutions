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
               r -= 1                                   #else decrease the right ptr
        return maxarea

#Time Complexity : O(n)
#Space Complexity: O(1)

#Dry Run
#height = 1, 8, 6, 2, 5, 4, 8, 3, 7] 
# l= 0, r = 8, maxarea = 0, 0< 8, yes , area = 1 * 8 = 8, maxarea = 8. 0< 8 l = 1
# l = 1, r =8, 1< 8 yes, area = 7 * 7 = 47 maxarea = 49, r = 7
# l = 1, r = 7, 1< 7 yes, area = 3* 6 = 18 maxarea = 49, r =6
# l =1, r = 6, 1< 6 yes, area = 8 *5 = 40 maxarea = 49, r = 5
# l = 1, r = 5, 1< 5 yes , area = 4 *4 = 16 maxarea = 49, r = 4
# l = 1, r = 4, 1< 4 yes, area = 5 * 3 = 15 , maxxarea = 49, r = 3
# l = 1, r = 3, 1< 3, yes, area= 2* 2 = 4, maxarea = 49, r = 2
# l = 1, r = 2, 1< 2, yes, area = 6 * 1= 6, maxarea= 49, r = 1
# loop ends result = maxarea = 49 
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


"""
Edge Cases
Only two lines: [1,1] → Area is 1
All lines same height: [5,5,5,5] → Max area = (n-1) * 5
Height contains zero: [0,1,2,3,4] → Ignore zero, as water is limited by smallest bar
Large array, varied heights: Algorithm remains O(n)

How to Explain in an Interview
Clarifying questions:
Can lines be at the same index? (No, must be different.)
Can height be zero? (Yes.)
Should I return the area or the indices? (Area.)

Approach (One-liner):
"Start two pointers at both ends, always move the shorter bar inward, since moving the taller one can't increase area, and keep track of the maximum area found."

Time & Space Complexity:
Time: O(n) (one pass from both ends)
Space: O(1) (just a few variables)
"""