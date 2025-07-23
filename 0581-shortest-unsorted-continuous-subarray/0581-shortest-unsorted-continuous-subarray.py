class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        start , end = -1, -2        #trick to get 0 if already sorted
        minsofar, maxsofar = nums[-1], nums[0]      # masx at start of array, min at the end of the array 

        for i in range(1, n):
            maxsofar = max(maxsofar, nums[i])
            if nums[i] < maxsofar:
                end = i
        for i in range(n-2, -1, -1):
            minsofar = min(minsofar, nums[i])
            if nums[i] > minsofar:
                start = i
        return end - start + 1
        