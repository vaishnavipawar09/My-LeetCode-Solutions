class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        i = 0
        for i in range(len(nums) - 2):
            l, r = i +1, len(nums) - 1
            while l< r:
                calsum = nums[i] + nums[l] + nums[r]
                if abs(calsum - target) < abs(closest - target):
                    closest = calsum
                if calsum < target:
                    l += 1
                elif calsum > target:
                    r -= 1
                else:
                    return calsum
        return closest

"""
Approach
Sort the input array.
Use a fixed pointer (i) and a two-pointer approach (left, right) to try all possible triplets efficiently.
Keep track of the sum closest to the target using a closest variable.
For every triplet, update closest if the current sum is nearer to the target.
If an exact match is found, return immediately.

Time & Space Complexity
Time: O(n²) — for each index, the inner two-pointer scan is linear.
Space: O(1) — we use only a few extra variables (apart from sorting, which is O(n log n)).

Edge Cases
Array contains negatives/positives/zeros: Works for all.
Duplicates: Handled automatically; we don’t care about uniqueness, just closest sum.
Exactly three numbers: That triplet is the answer.

Dry Run (Example)
Input: nums = [-1,2,1,-4], target = 1
Sorted: [-4, -1, 1, 2]
i = 0 (num=-4), left=1 (num=-1), right=3 (num=2)
curr_sum = -4 + -1 + 2 = -3 (closest so far: -3)
-3 < 1, move left pointer: left=2 (num=1)
curr_sum = -4 + 1 + 2 = -1 (closer, update closest to -1)
-1 < 1, left=3 (left == right, break)
i = 1 (num=-1), left=2 (num=1), right=3 (num=2)
curr_sum = -1 + 1 + 2 = 2 (closer, update closest to 2)
2 > 1, move right pointer: right=2 (left == right, break)

Result: 2 (as expected)

Interview "Statement to Remember"
"Sort, then for each number use two pointers to scan for the closest sum—updating the answer whenever a new closest is found. O(n²) time."

"""