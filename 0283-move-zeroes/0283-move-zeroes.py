class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0 
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1
        for i in range(k , len(nums)):
            nums[i] = 0
#Time Complexity : O(n)
#Space Complexity : O(1)
        """ You move non-zeroes up front, but you forgot to fill the rest with zeroes. After your loop, the end of the array still has old values. Next, you should set all elements from index k to the end as zero.
        """