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

     
        