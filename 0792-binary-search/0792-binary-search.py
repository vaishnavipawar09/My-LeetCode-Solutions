class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0                   #intialize two pointers left start of array and right at the end of array
        r = len(nums) - 1

        while(l <= r):          #loop through the array if l <= r
            mid = (l + r) // 2  #Calculate the mid val of each array/ subarray

            if nums[mid] == target: #If target found, return mid which is the index of the target
                return mid
            
            if nums[mid] < target:  #if mid val is less than target then move to right subarray
                l = mid + 1         #To move to right subarray, change left ptr to mid + 1
            else:
                r = mid - 1         #Mov to left subarray if target less than mid 
        return -1                   #Return -1 that is if target not found

        #Time Complexity: O(logn)
        #Space Complexity: O(1) as this is iterative binary search



