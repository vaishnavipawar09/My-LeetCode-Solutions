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


#Time Complexity: O(n)
#Space Complexity: O(1)

#Dry Run nums = [1, 1, 1, 2, 2, 3]
#. k = 0, i = 0, i < 6, k< 0< 2 yes, nums[k]= nums[i] nums[0] = 1, k =1         nums= [1, 1, 1, 2, 2, 3]
# k = 1, i = 1, 1< 6, 1< 2 yes, nums[k] = nums[i] nums[1] = 1, k =2             nums= [1, 1, 1, 2, 2, 3]
# k = 2, i = 2, 2< 6, 2< 2 no, else, nums[i] != nums[k-2] nums[2] != nums[0] 1!=1 no, cause they are equal, skip
# k = 2, i =3 2<2 no, else nums[3] != nums[0] 2!= 1 yes, nums[2] = 2, k = 3     nums = [1, 1, 2, 2, 2, 3]
# k = 3, i = 4, 4<6, 2<2 no, else nums[4] != nums[1], 2!= 1 yes, nums[3] = 2, k = 4 nums= [1, 1, 2, 2, 2, 3]
# k = 4, i =5, 5<6, 4< 2 no, else nums[5] != nums[2] 3!= 2, yes, nums[4] = 3, k = 5 nums = [1, 1, 2, 2, 3, 3]
# k = 5 , i =6, 6< 6 no, break out of for loop return k , here k is 5
#Output = 5
