class Solution:
    def rob(self, nums: List[int]) -> int:
        # Initialize two variables:
        # rob1 stores max amount robbed up to house i-2
        # rob2 stores max amount robbed up to house i-1
        rob1, rob2 = 0, 0

        # Iterate through each house in nums
        for num in nums:
            # For the current house, we decide:
            # - rob it: add current house money to rob1 (which is up to i-2)
            # - skip it: just take rob2 (which is up to i-1)
            # We want the maximum of these two choices.
            temp = max(num + rob1, rob2)
            # Update rob1 to be the previous rob2 (move window forward)
            rob1 = rob2
            # Update rob2 to be the new max up to this house
            rob2 = temp

        # At the end, rob2 contains the max money robbed from all houses
        return rob2

        '''
        --- Dry Run Example ---
        nums = [2,9,8,3,6]
        rob1 = 0, rob2 = 0

        Step 0: num = 2
            temp = max(2 + 0, 0) = 2
            rob1 = 0
            rob2 = 2

        Step 1: num = 9
            temp = max(9 + 0, 2) = 9
            rob1 = 2
            rob2 = 9

        Step 2: num = 8
            temp = max(8 + 2, 9) = 10
            rob1 = 9
            rob2 = 10

        Step 3: num = 3
            temp = max(3 + 9, 10) = 12
            rob1 = 10
            rob2 = 12

        Step 4: num = 6
            temp = max(6 + 10, 12) = 16
            rob1 = 12
            rob2 = 16

        Output: 16

        --- Time Complexity ---
        O(n)    # One loop through nums

        --- Space Complexity ---
        O(1)    # Only two variables used, no extra arrays
        '''
