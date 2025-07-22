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


"""
#Clarifying Questions
Can I use extra space?No, must be in-place.
Is the array always sorted?Yes, non-decreasing.
What do I return?Return the count of unique elements (k).
Do I need to care about what is in nums after the first k elements?No, can be anything.

#Approach (Two Pointers)
Use one pointer i for the current unique spot (where the next unique element should go).
Use another pointer j to scan the array.
If nums[j] != nums[i], increment i and set nums[i] = nums[j].
Finally, return i + 1 (since i is index-based).

Time & Space Complexity
Time: O(n) (one pass)
Space: O(1) (in-place)

Edge Cases
[1] → 1
[1,1,1,1] → 1
[] → 0

"""