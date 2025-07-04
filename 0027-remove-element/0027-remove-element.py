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

#Dry Run
# nums = [3, 2, 2, 3], val = 3, k = 0
# 1. k = 0, i = 0, nums[i] != val ie nums[0] !=val ie 3 != 3 no so break loop and increase i i = 1
# 2. k = o, i = 1, nums[1] !=val ie, 2 != 3 yes, nums[k] = nums [i] ie nums[0] = nums[1] = nums[0] = 2, k =1, i =2  nums= [2,]
# 3. k =1, i =2, nums[2] !=val ie 2 != 3 yes, nums[1] = nums[2], nums[1] = 2, k =2, i = 3   nums = [2, 2]
# 4. k = 2, i =3, nums[3] ! = val, 3!=3 no, break , i =4        
# 5. i = 4 the loop doesnt execute cause it is over 
# 6. return k , currently k = 2 return k Output is 2