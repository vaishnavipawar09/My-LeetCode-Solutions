class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = []
        r = 0  # unjudged minimum index
        n = len(nums)
        for j in range(n):
            if nums[j] == key:
                l = max(r, j - k)
                r = min(n - 1, j + k) + 1
                for i in range(l, r):
                    res.append(i)
        return res



"""
Clarifying Questions
Is nums guaranteed non-empty? (Yes, per constraints.)
Can key appear multiple times? (Yes.)
Should the output be sorted and have no duplicates? (Yes, explicitly stated.)
Are negative numbers possible? (No, all values ≥ 1.)
Can k equal the length of the array? (Yes.)

Optimal Approach (Interview Style)
High-level Plan
Find all indices where nums[i] == key.
For each such index, mark all indices within k distance.
Use a set to avoid duplicates.
Return the sorted list.

Line-by-line Explanation
Loop through all indices. If nums[j] == key, then all indices from j-k to j+k (bounded within [0, n-1]) are valid.
Add each such index to a set to avoid duplicates.
Return the sorted result.

Time Complexity
O(n * k), worst case (if every element is key).
But for reasonable k (and the given constraint n <= 1000), this is perfectly fine.

Edge Cases
If all elements are key, every index will be k-distant.
If key appears only once, only indices near that one index are included.
Handles the edges by capping with max(0, ...) and min(n, ...).

One-liner to Remember
"For each occurrence of key, mark all indices within k distance, and return the sorted unique set."


"""