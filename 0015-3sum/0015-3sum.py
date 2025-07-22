class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []                                    #Return the result in the form of list hence []
        nums.sort()                                 #Sort the array

        i = 0                                       
        for i in range(len(nums)):                  #Iterates through the array
            if i > 0 and nums[i] == nums[i - 1]:    #If duplicates, move forward, i is at start 
                continue

            j, k = i + 1, len(nums) - 1             #Create left and right pointer, left is i +1, cause i!=j

            while j < k:
                calsum = nums[i] + nums[j] + nums[k] #Calculate the three sum
                if  calsum < 0:                     #Sum < 0, increase the left pointer by 1
                    j += 1
                elif calsum > 0:                    #Sum > 0, decrease the right pointer by 1
                    k -=1
                else:                               #If sum == 0, add the values in the array
                    res.append([nums[i], nums[j], nums[k]]) # add to te result
                    j += 1                          #Update the pointers j and k
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]: #Duplicate, so shift our pointer
                        j += 1
                    
        return res                                  #return the result


#Time Complexity: O(n^2)    (one loop takes nlog n and the other j, k loop takes n^2 so total it is n^2)
#Space Complexity: O(1) or O(n) depends upon sorting algorithm

#Dry Run:
#For nums = [-1,0,1,2,-1,-4]:
#After sort: [-4, -1, -1, 0, 1, 2]
#i=0, nums[i]=-4: left=1, right=5 (no triplet sums to 0) -4 + -1  + (-1) = -7 < 0  Left = 2
# i = 0, l = 2, r = 5, -4 + -1 + -1 = -7 < -1 left = 3
# i = 0, l = 3, r = 5, -4 + 0 +2 = -2 < 0 left = 4
# i = 0, l = 4, r = 5 4 < 5 yes, -4 + 1 + 2 = -1 < 0 , left + 1 = 5 
# i = 0, l = 5, r= 5, 5 == 5 no loop
# i = 1, l = 2, r = 5 2< 5 yes, -1 +  -1 + 0 + -4 = -5 no
#  [-1, -1, 2] [-1, 0 , 1]
"""
1. Clarifying Questions
Can the array contain duplicates? Yes, but no duplicate triplets in the answer
Can I use extra space? Yes
Should output order matter? No
Must indices be different? Yes, i != j != k

2. Test Cases
[-1,0,1,2,-1,-4] → [[-1,-1,2], [-1,0,1]]
[0,1,1] → []
[0,0,0] → [[0,0,0]]
[1,2,-2,-1] → []

3. Approach
Sort the array.
Loop through the array:
For each index i, use two pointers (left and right) to find pairs such that nums[i] + nums[left] + nums[right] == 0.
Skip duplicates for both i and the two pointers to ensure unique triplets.

5. Edge Cases
All zeroes ([0,0,0,0,0]) → should return [[0,0,0]]
No solution exists ([1,2,3]) → []
Duplicates in array ([-2,0,1,1,2]) → only unique triplets

6. Time and Space Complexity
Time: O(n^2) (for each i, two pointers scan the rest)
Space: O(n) for sorting (could be O(1) extra if in-place), plus O(k) for output.
"""



