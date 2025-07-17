
class Solution:
    def climbStairs(self, n: int) -> int:
        # Implementation Steps:
        # 1. Initialize two variables, `one` and `two`, to 1.
        #    - `one` will store the number of ways to reach step i+1.
        #    - `two` will store the number of ways to reach step i.
        one, two = 1, 1

        # 2. Loop from 0 to n-2 (because for n=1, answer is 1, and for n=2, answer is 2).
        for i in range(n - 1):
            temp = one            # Store current 'one' to update 'two' later
            one = one + two       # The current number of ways is sum of previous two steps
            two = temp            # Update 'two' to the previous 'one' for next iteration

        return one                # 3. Return 'one', which now holds the number of ways to reach step n

        '''
        Dry Run:
        Example: n = 4
        Initial: one = 1, two = 1

        Loop 1 (i=0):
          temp = 1
          one = 1 + 1 = 2
          two = 1

        Loop 2 (i=1):
          temp = 2
          one = 2 + 1 = 3
          two = 2

        Loop 3 (i=2):
          temp = 3
          one = 3 + 2 = 5
          two = 3

        End: return one = 5

        For n=4, Output = 5
        Ways: [1,1,1,1], [2,1,1], [1,2,1], [1,1,2], [2,2]

        Time Complexity:
        - O(n): The loop runs n-1 times

        Space Complexity:
        - O(1): Only two variables are used, regardless of n

        Interview Notes:
        - This is optimal for just the number of ways. No extra array is needed.
        - The problem is a classic Fibonacci sequence application.
        '''
