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