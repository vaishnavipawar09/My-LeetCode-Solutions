class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0                           #start of the array           
        r = len(nums) - 1               #end of the array

        while(l<r):                     #use l<r instead of l<=r cause we stop when l==r
            mid = (l + r) // 2          #cal the mid pt of array

            if nums[mid] > nums[r]:     #if mid val is greater than the right value
                l = mid + 1             #increase the left ptr mid + 1(right subarray)
            else:                       #nums[mid] < nums[l]:
                r = mid                 #mid , cause mid can be the min instead so do not use mid - 1
                                        #we do not use l == r cause all values are unique
        return nums[l]                  #cause l points to the minimum


#Time Complexity: O(log n)
#Space Complexity: O(1)