class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0                               # Write pointer for where to put the next allowed number

        for i in range(len(nums)):          #iterate the array
            if k < 2:                       #Cause only two duplicates allowed, run until k < 2
                nums[k] = nums[i]           #add the two values to the list
                k+=1                        #increment k
            elif nums[i] != nums[k-2]:      #if nums[i] is unique then the last two value we have seen
                nums[k] = nums[i]           #For the 3rd and onwards, only keep if not equal to a third duplicate)
                k+=1                        #increment k
                
        return k                            # Length of array with each value at most twice