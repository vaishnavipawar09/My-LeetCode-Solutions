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

#Dry RUn
#NUMS = [2, 2, 1, 1, 1, 2, 2]
#1. res = 0, cnt = 0, n = 2, cnt == 0, 0 ==0 yes, res = 2, 2 == res(2) yes, cnt = 1
# 2. res = 2, cnt = 1, n = 2, 1 == 0 no, 2 ==2 yes, cnt = 2
# 3. res = 2, cnt = 2, n = 1, 2 == 0 no, 1 == 2 , no , cnt -= 1, cnt = 1
# 4. res = 2, cnt =1, n = 1, 1 ==0 , no, 1 == 2 no, cnt = 0
# 5. res = 2, cnt = 0, n = 1, 0 == 0 yes, res = 1, 1 == 1 yes, cnt = 1
# 6. res = 1, cnt = 1, n= 2, 1 == 0 no, res = 1,1 == 2 no, cnt -=1 cnt = 0
# 7. res = 1, cnt = 0, n = 2, 0 == 0 yes, res = 2, 2 == 2 yes, cnt = 1
# 8. no more n in mums exit loop , return res = 2 Output = 2