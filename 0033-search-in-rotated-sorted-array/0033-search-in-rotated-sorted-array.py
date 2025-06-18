class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0                                       #start of array
        r = len(nums) - 1                           #end of array

        while(l<=r):                                #loop though whole array till l<=r
            mid = (l + r) // 2                      #cal mid value of the array

            if nums[mid] == target:                 #if target found return the mid value
                return mid

            #decide which half is sorted first
            if nums[l] <= nums[mid]:                        #this is if left subarray is sorted
                if target > nums[mid] or target < nums[l]:  #Check if target is between nums[l] and nums[mid]
                    l = mid + 1                             #if yes shift left ptr
                else:
                    r = mid - 1                             #if target not found bet them shift right ptr
            else:                                           #if right subarray is sorted
                if target < nums[mid] or target > nums[r]:  #Check if target is between nums[r] and nums[mid]
                    r = mid - 1                             #if yes shift right ptr
                else:
                    l = mid + 1                             #not found sift left ptr
        return -1                                   #If target not found return -1

#Time Complexity: O(log n)
#Space Complexity: O(1)