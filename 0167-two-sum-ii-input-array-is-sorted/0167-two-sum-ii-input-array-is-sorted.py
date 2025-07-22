class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1                  #Created two pointers, left and right
        while l < r:                                #Loop through the array
            currsum = numbers[l] + numbers[r]       #Check the current sum
            if currsum == target:                   #Check if sum = target and return index added by one
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:  #If sum < target, increment l by 1
                l = l + 1
            else:                                   #If sum> target, dercrement r by 1
                r = r - 1
        return []

#Time Complexity: O(n)    Loops through the array of n intergers
#Space Complexity: O(1)   No extra space needed, only two pointers

      
#Dry Run, numbers = [2, 7, 11, 15], target = 9
# 1. l = 0, r = 3, 0< 3 yes, currsum = 17 , 17 ==9 no, elif 17 < 9 no, else r = 2
# 2. l = 0, r = 2, 0< 2 yes, currsum = 13,13 == 9 no, elif 13< 9 no , else r = 1
# 3. l = 0, r = 1, 0< 1 yes, currsum = 9 , 9 == 9 yes, return [1, 2]

# With -ve and 0 , numbers = [-1, 0, 1] Target = -1
# 1. l = 0, r = 2, 0< 2 yes, currsum = 0, 0 ==-1 no, 0< -1 no , else r = 1
# 2. l = 0, r = 1, 0< 1 yes, currsum = -1, -1 == -1 yes, return [1, 2]


"""
1. Clarifying Questions
Is the array sorted? Yes
Can I use extra space? No, must be O(1) space
Are negative numbers allowed? Yes
Will there always be exactly one solution? Yes, per constraints
Indices should be 1-based, right? Yes

2. Test Cases
[2,7,11,15], target=9 → [1,2]
[2,3,4], target=6 → [1,3]
[-1,0], target=-1 → [1,2]
[1,2,3,4,4], target=8 → [4,5]

3. Approach
Since the array is sorted, use two pointers:
left at 0 (start), right at len(numbers)-1 (end)
While left < right:
Calculate sum = numbers[left] + numbers[right]
If sum == target: return [left+1, right+1] (convert to 1-based)
If sum < target: move left forward
If sum > target: move right backward

5. Edge Cases
Only two elements (always valid per constraints).
Target sum is negative or zero.
Large numbers at array ends.
"""