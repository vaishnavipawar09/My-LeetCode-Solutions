class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0               #Use two ptr, slow and fast, start at 0
        while True:                     #keep going until they intersect
            slow = nums[slow]           #Tortoise moves slow, one jump
            fast = nums[nums[fast]]     #Hare moves i = nums[nums[i]], two jump
            if slow == fast:            #if they match, break we found one cycle
                break

        slow2 = 0                       #use second slow ptr, until it intersects with the other slow ptr
        while True:
            slow = nums[slow]           #both slow ptr move by one step, until it intersects
            slow2 = nums[slow2]
            if slow == slow2:           #If interects we will find the duplicate
                return slow

#Time Complexity: O(n)
#Space Complexity: O(1)

#Dry Run: nums = [1, 3, 4, 2, 2]
#s = 0, f = 0. s = 1, f = 4, 1 == 4 no 
# s = 3, f = 2 3 == 2 no 
# s = 4, f = 3, 4==3 no
# s = 2, f = 2, 2==2 yes break found the cycle

# s = 2, s2 = 1 2 == 1 no, 
# s = 2, s2 = 3 2 == 3 no
# s = 2, s2 = 4 2 ==4 no 
# s = 2, s2 = 2 2==2 yes
# return s = 2

"""
#Clarifying Questions
Can I modify the input array? (No, per constraints)
Can I use extra space? (Only O(1) extra)
Are negative numbers possible? (No, values from 1 to n)
Is there always exactly one duplicate? (Yes)
Are there guaranteed at least two occurrences of the duplicate? (Yes, can be more than two)

Key Insight
Why Floyd’s Tortoise and Hare?
The numbers form an implicit linked list:
index -> value at index
(each value is a "next" pointer, since all values in [1, n]).
By the Pigeonhole Principle, there must be a cycle—the duplicate is the cycle's entry.

Line by Line Explanation
Initialize slow and fast to the first value (nums[0])
Move slow by one step, fast by two until they meet (cycle detected)
Reset slow to the beginning, move both one step at a time
The node (value) where they meet is the duplicate

Why does a duplicate always exist?
There are n+1 entries but only n values (from 1 to n). By the pigeonhole principle, at least one value is repeated.
"""