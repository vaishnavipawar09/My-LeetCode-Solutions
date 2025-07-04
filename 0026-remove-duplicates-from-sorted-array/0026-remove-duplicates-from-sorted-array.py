class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1                           #Intitilize k = 1, since first element is always unique

        for i in range(len(nums)):      #iterate through the whole array
            if nums[i] != nums[k - 1]:  #if nums[i] is unique then the last value we have seen  
                nums[k] = nums[i]       #Store the non target element at the curr index
                k += 1                  #increment the index by 1, move to the next position
        return k                        #return the total count of elements in the array , without val
        
#Time Complexity: O(n)
#Space Complexity: O(1)

#Dry Run : nums = [1, 1, 2]
# 1. k  1, i = 0, nums[0] != nums[0], 1 != 1, no , i = 1 ,  nums = [1, 1, 2]
# 2. k =1, i = 1, nums[1] ! = nums[0], 1 !=1 no, i = 2, nums = [1, 1, 2]
# 3. k = 1, i = 2, nums[2] != nums[0], 2 != 1, yes, nums[1] = nums[2] = 2, k = 2 nums = [1, 2 , 2]
# 4. k =2, i = 3, the max length was 2 , not allowed, k = 2, output is k = 2