class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # in place
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = reversed(nums[i + 1:])

"""
Start from the end: 2 < 3, so i = 1.
Find next biggest: 3 > 2, so j = 2.
Swap: [1, 3, 2].
Reverse after i: nothing to reverse, so result is [1, 3, 2].
"""

#Time Complexity : O(n)
#Space Complexity : O(1)