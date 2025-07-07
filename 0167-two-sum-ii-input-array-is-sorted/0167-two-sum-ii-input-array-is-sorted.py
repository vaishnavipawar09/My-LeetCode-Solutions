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
#Space Complexity: O(1)   No extra space needed

      
#Dry Run, numbers = [2, 7, 11, 15], target = 9
# 1. l = 0, r = 3, 0< 3 yes, currsum = 17 , 17 ==9 no, elif 17 < 9 no, else r = 2
# 2. l = 0, r = 2, 0< 2 yes, currsum = 13,13 == 9 no, elif 13< 9 no , else r = 1
# 3. l = 0, r = 1, 0< 1 yes, currsum = 9 , 9 == 9 yes, return [1, 2]

# With -ve and 0 , numbers = [-1, 0, 1] Target = -1
# 1. l = 0, r = 2, 0< 2 yes, currsum = 0, 0 ==-1 no, 0< -1 no , else r = 1
# 2. l = 0, r = 1, 0< 1 yes, currsum = -1, -1 == -1 yes, return [1, 2]