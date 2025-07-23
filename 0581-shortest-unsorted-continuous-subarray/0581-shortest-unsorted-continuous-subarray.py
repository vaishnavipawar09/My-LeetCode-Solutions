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
        
"""
Optimal O(n) Solution — Monotonic Scan
Key Idea:
If the array is not sorted, there will be a left boundary where the order breaks and a right boundary where the order resumes.
The leftmost index where the array is greater than the min to its right, and the rightmost index where the array is less than the max to its left, defines the boundaries to sort.

Algorithm Steps
Find the left boundary:
Scan from left to right, keeping track of the max seen so far. If nums[i] < max_so_far, mark end = i.
Find the right boundary:
Scan from right to left, keeping track of the min seen so far. If nums[i] > min_so_far, mark start = i.
If the array is already sorted, end and start won't be set meaningfully — just return 0.
Otherwise, the length is end - start + 1.

Line by Line Explanation
Left to right: If current number is smaller than max so far, it’s out of order — update end.
Right to left: If current number is bigger than min so far, it’s out of order — update start.
If nothing is out of order, start = -1, end = -2 so end - start + 1 = 0.
Else, return the length.

Edge Cases
Already sorted: [1,2,3,4] ➔ 0
Single element: [1] ➔ 0
Entire array unsorted: [2,1] ➔ 2

One-liner to Remember
"Find the smallest window (start to end) where any number to the left is ≤ min in window, and any number to the right is ≥ max in window."

"""