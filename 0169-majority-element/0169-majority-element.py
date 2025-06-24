class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result, cnt= 0,0            #initialized a candidate variable and counter

        for n in nums:              #step 2
            if cnt == 0:            #step 2.1
                result = n
            if n == result:         #step 2.2
                cnt += 1
            else:
                cnt -= 1            #step 2.3
        
        return result               #step 4



"""
Boyer-Moore Voting Algorithm Explanation:

- Goal: Find the majority element in an array (the element that appears more than n // 2 times).
- Approach: Use a single pass through the array and only O(1) extra space.

How it works:
1. Initialize a candidate variable for the majority element and a counter.
2. Loop through the array:
    - If the counter is zero, set the current number as the new candidate.
    - If the current number is the same as the candidate, increment the counter.
    - If the current number is different, decrement the counter.
3. Intuition: Pairs of different elements "cancel each other out." 
    Because the majority element occurs more than half the time, it will always be the final candidate remaining after all cancellations.
4. Result: At the end of the loop, the candidate is the majority element.

Time Complexity: O(n)
Space Complexity: O(1)
"""

