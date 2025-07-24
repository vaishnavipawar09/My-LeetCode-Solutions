class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0 
        charSet = set()
        currsum = 0
        maxscore = 0
        for r in range(len(nums)):
            while nums[r] in charSet:
                charSet.remove(nums[l])
                currsum -= nums[l]
                l +=1
            charSet.add(nums[r])
            currsum += nums[r]
            maxscore = max(maxscore, currsum)

        return maxscore

#Easy same as find palindrome, just calculate the valeues from the hashset

"""
Clarifying Questions
Can numbers repeat?
Yes, and you want only unique elements in the subarray.

Can I use extra space?
Yes, use a set or map.

What to return if all elements are unique?
Return the sum of the entire array.

Approach (Sliding Window + Set)
Use a sliding window with a set to maintain unique elements; move the left pointer to remove duplicates, updating the current sum and the max sum as you go.

Dry Run
Example: nums = [4,2,4,5,6]
right = 0, nums[0]=4 → seen: {4}, curr_sum=4, max_sum=4
right = 1, nums[1]=2 → seen: {2,4}, curr_sum=6, max_sum=6
right = 2, nums[2]=4 (duplicate)
Remove nums[0]=4 from set, curr_sum=2, left=1
Add 4: seen={2,4}, curr_sum=6
right = 3, nums[3]=5 → seen: {2,4,5}, curr_sum=11, max_sum=11
right = 4, nums[4]=6 → seen: {2,4,5,6}, curr_sum=17, max_sum=17
Final answer: 17

Edge Cases
All elements unique: Return sum of all.
All elements same: Return value of one element.
Large input: Still O(n) time and space.

One-liner to Remember
"Sliding window with a set: Move left pointer to maintain uniqueness, track max sum."
"""