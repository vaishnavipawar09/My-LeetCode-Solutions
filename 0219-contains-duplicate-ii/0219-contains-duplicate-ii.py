class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        for i, num in enumerate(nums):
            if num in seen:
                return True
            seen.add(num)
            if len(seen) > k:
                seen.remove(nums[i - k])
        return False


"""
Clarifying Questions:
Can the input array be empty? (No, since nums.length ≥ 1)
Are negative numbers or zeros allowed in the array? (Yes)
Should I return False if k is 0? (Yes, because indices can’t be the same)
What if multiple pairs qualify? (Return True on the first one found)
What’s the expected time and space complexity? (Optimal solution is O(n) time, O(k) space)

Approach (Optimal):
Sliding Window + Hash Set:
Keep a hash set of the last k seen elements.
For each number in nums:
If the number is already in the set, return True (duplicate within window).
Add the number to the set.
If the set size exceeds k, remove the oldest number (slide the window).
If no duplicates found, return False.

Dry Run (Example 1):
nums = [1,2,3,1], k = 3
i=0: num=1, seen={} ⇒ Add 1 → seen={1}
i=1: num=2, seen={1} ⇒ Add 2 → seen={1,2}
i=2: num=3, seen={1,2} ⇒ Add 3 → seen={1,2,3}
i=3: num=1, seen={1,2,3} ⇒ 1 in seen ⇒ return True

Edge Cases:
k = 0: Always False (no two indices can have distance ≤ 0).
No duplicates: Return False.
Window size exceeds array: The sliding window just covers the whole array.

Time and Space Complexity:
Time: O(n) — each element is added/removed from set at most once.
Space: O(min(n, k)) — the hash set holds at most k elements.

One-Liner Statement to Remember:
“Use a sliding window set of size k to check for duplicates within distance k.”
"""