class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, quad = [], []

        #helper function for ksum if k changes
        def kSum(k, start, target):
            if k != 2: 
                for i in range(start, len(nums) - k +1):
                    if i > start and nums[i] == nums[i-1]:
                        continue        
                    quad.append(nums[i])
                    kSum(k -1, i + 1, target - nums[i])
                    quad.pop()
                return

            l, r = start, len(nums) - 1
            while l< r:
                if nums[l] + nums[r] < target:
                    l +=1
                elif nums[l] + nums[r] > target:
                    r -=1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l +=1
                    while l< r and nums[l] == nums[l-1]:
                        l +=1
        kSum(4, 0, target)
        return res

"""
Approach:
This is a generalization of the 2Sum/3Sum problem. The idea is to:
Sort the array to make it easier to avoid duplicates and use two pointers.
Use four pointers: The outer two (i and j) loop through the array, and the inner two (left and right) search for pairs that sum to the required value.
Skip duplicates at every step to avoid repeated quadruplets.

How It Works (Step-by-Step):
Sort nums for easier duplicate handling and two-pointer use.
Outer loops (i, j) fix the first two numbers.
Inner two pointers (left, right) scan the rest of the array for pairs that sum to target - (nums[i] + nums[j]).
If a quadruplet is found, add it, then skip any duplicates.
Continue searching until all unique quadruplets are found.

Time Complexity:
O(n³): Three nested loops in the worst case (outer two and two-pointer scan).

Edge Cases:
Less than 4 numbers: Return []
Duplicates: Handled by skipping over same values for each pointer.
Large/small numbers: No special handling needed; Python ints can handle big numbers.

Example Dry Run
Input: nums = [1,0,-1,0,-2,2], target = 0
Sorted: [-2, -1, 0, 0, 1, 2]
i = 0 (-2), j = 1 (-1), left = 2 (0), right = 5 (2)
sum = -2 + -1 + 0 + 2 = -1 < 0 → left++
sum = -2 + -1 + 0 + 2 = -1 < 0 → left++
sum = -2 + -1 + 1 + 2 = 0 → found quadruplet, add [-2,-1,1,2]
Move pointers, skip duplicates, repeat...
Continue with all possible i/j, collect all valid unique quadruplets.

Statement to Remember
"Sort the array, use two nested loops and two pointers, and skip duplicates to find all unique quadruplets that sum to the target."


"""