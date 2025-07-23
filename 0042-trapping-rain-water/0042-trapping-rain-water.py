class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0  # Edge case: if the input list is empty, no water can be trapped

        l, r = 0, len(height) - 1                  # Initialize two pointers at both ends
        leftMax, rightMax = height[l], height[r]  # Set initial left and right maximums
        res = 0                                    # Variable to store total trapped water

        while l < r:                               # Loop until the two pointers meet
            if leftMax < rightMax:                # Process the side with the smaller max
                l += 1                             # Move the left pointer inward
                leftMax = max(leftMax, height[l])  # Update the left maximum
                res += leftMax - height[l]         # Water trapped = leftMax - current height
            else:
                r -= 1                             # Move the right pointer inward
                rightMax = max(rightMax, height[r])# Update the right maximum
                res += rightMax - height[r]        # Water trapped = rightMax - current height

        return res                                 # Return the total trapped water

#Time Complexity: O(n)
#Space Complexity: O(1)
# Dry Run:
#[4, 2, 0, 3, 2, 5]
# l = 0, r = 5 maxleft = 4, maxright = 5, res = 0, 0< 5 yes, 4< 5: l = 1, leftmax = 4, res = 4-2 = 2
# l = 1, r = 5, maxleft = 4., rightmax = 5, 4< 5, l = 2, leftmax= 4, res = 4- 0 = 4 res = 4=2 = 6
# l = 2, r = 5, maxl =4, maxr= 5, 4< 5, l = 3, maxl = 4, res = 4 - 3 =1, = 6 = 7
# l = 3, r = 5, maxl= 4, maxr = 5, 4< 5, l = 4, res = 4 - 2 = 2 + 7 = 9
# l = 5, r = 5, loop ends res = 9 which is the output! 
        """ Solved: 
        if not height: return 0
        
        l, r = 0, len(height) - 1                   #Two pointers , left and right
        leftmax, rightmax = 0, 0                    #Cal max val of left and right
        totalwater = 0                              #Cal total water 

        while l < r:                                # Process while pointers haven't crossed
            if height[l] < height[r]:               # Decide pointer movement based on smaller height
                if height[l] < leftmax:             # If current height is lower than max on the left
                    totalwater += leftmax - height[l]  # Water can be trapped: add the difference
                else:
                    leftmax = height[l]             # Update leftmax if current height is higher
                l += 1                              # Move left pointer by 1
            else:
                if height[r] < rightmax:            # If current height is lower than max on the right
                    totalwater += rightmax - height[r]  # Water can be trapped: add the difference
                else:
                    rightmax = height[r]            # Update rightmax if current height is higher
                r -= 1                              # Move right pointer by 1, decrease it

        return totalwater                           # Return the total amount of trapped water

"""
