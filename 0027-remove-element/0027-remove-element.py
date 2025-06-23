class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0                           #Intialize k to track the total elements
        for i in range(len(nums)):      #iterate through the whole array
            if nums[i] != val:          #if the curr value doesnt match the required value, iterate
                nums[k] = nums[i]       #Store the non target element at the curr index
                k += 1                  #increment the index by 1, move to the next position
        return k                        #return the total count of elements in the array , without val
        
#Time COmplexity: O(n)
#space Complexity: O(1)