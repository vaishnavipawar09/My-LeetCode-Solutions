class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        #This is using the same idea of Partition using of Quick Sort 
        """
        l, r = 0, len(nums)-1
        i = 0

        def swap(i, j):
            temp= nums[i]
            nums[i]= nums[j]
            nums[j] = temp

        while i<=r:
            if nums[i]==0:
                swap(l, i)
                l+=1        
            elif nums[i]==2:
                swap(i, r)
                r-=1
                i-=1
            i+=1


"""
0's: Move to the left.
2's: Move to the right.
1's: Stay in the middle.

Edge Cases
All elements are the same: [0,0,0] or [2,2,2] (should remain unchanged)
Only one element: [1]
Already sorted: [0,0,1,1,2,2]
Reverse order: [2,2,1,1,0,0]
Random mix: [2,0,1]

How to Explain in an Interview
Clarifying questions:
Can I use extra space? (No, must be in-place.)
What values will nums contain? (Only 0, 1, 2)
Any constraints on length? (1 ≤ n ≤ 300)

One-liner approach:
"Partition the array into three sections for 0's, 1's, and 2's using three pointers, swapping elements as needed in a single pass."

Time & Space Complexity:
Time: O(n) — each element is checked at most once.
Space: O(1) — only constant extra variables.
"""