class Solution:
    def rob(self, nums: List[int]) -> int:
        # Since houses are in a circle, can't rob both first and last
        # Case 1: Exclude last house, rob from 0 to n-2
        # Case 2: Exclude first house, rob from 1 to n-1
        # Return the max of both cases
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1])) #if only one house, take that max too, exclude first house, exclude the last house

    def helper(self, nums):     # Standard House Robber for linear street
        rob1, rob2 = 0, 0

        for num in nums:
            temp = max(num + rob1, rob2)         # At each step, decide to rob this house (add to rob1) or skip (rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        # Handle edge case: only one house
        if len(nums) == 1:
            return nums[0]
        
        # Since houses are in a circle, can't rob both first and last
        # Case 1: Exclude last house, rob from 0 to n-2
        # Case 2: Exclude first house, rob from 1 to n-1
        # Return the max of both cases
        return max(
            self.helper(nums[1:]),      # Exclude first house
            self.helper(nums[:-1])      # Exclude last house
        )

    def helper(self, nums):
        # Standard House Robber for linear street
        rob1, rob2 = 0, 0
        for num in nums:
            # At each step, decide to rob this house (add to rob1) or skip (rob2)
            temp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

    '''
    --- Implementation Steps ---
    1. If there is only one house, return its value.
    2. Otherwise, consider two scenarios:
       a. Rob houses from index 0 to n-2 (exclude last).
       b. Rob houses from index 1 to n-1 (exclude first).
    3. For each scenario, use helper() to calculate max robbery.
    4. Return the maximum of both scenarios.

    --- Dry Run Example ---
    nums = [2, 3, 2]
    - helper(nums[1:]) = helper([3,2])
      rob1 = 0, rob2 = 0
      num = 3: temp = max(0+3, 0) = 3; rob1=0, rob2=3
      num = 2: temp = max(0+2, 3) = 3; rob1=3, rob2=3
      => result = 3

    - helper(nums[:-1]) = helper([2,3])
      rob1 = 0, rob2 = 0
      num = 2: temp = max(0+2, 0) = 2; rob1=0, rob2=2
      num = 3: temp = max(0+3, 2) = 3; rob1=2, rob2=3
      => result = 3

    Return max(3, 3) = 3

    --- Time Complexity ---
    O(n), where n is the length of nums. Two passes of House Robber (each O(n)).

    --- Space Complexity ---
    O(1), only a few variables used.

    --- Interview Note ---
    - When houses are in a circle, just run House Robber twice: once skipping first, once skipping last.
    - Say out loud: “This ensures we never rob both the first and last house, which are adjacent in a circle.”
    '''
"""