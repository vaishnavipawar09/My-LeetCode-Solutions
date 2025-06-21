class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]           #Tortoise moves slow, one jump
            fast = nums[nums[fast]]     #Hare moves i = nums[nums[i]], two jump
            if slow == fast:            #if they match, break we found one cycle
                break

        slow2 = 0                       #use second slow ptr, until it intersects with the other slow ptr
        while True:
            slow = nums[slow]           #both slow ptr move by one step
            slow2 = nums[slow2]
            if slow == slow2:           #If interects we will find the duplicate
                return slow

#Time Complexity: O(n)
#Space Complexity: O(1)