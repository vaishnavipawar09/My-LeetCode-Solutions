class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Implementation Steps:
        # 1. We append a zero to the end of the array to represent "the top" (no cost to step off).
        cost.append(0)

        # 2. We work backwards from the third-last index to the start (bottom-up DP).
        #    For each position, update cost[i] to be the cost at step i + 
        #    the minimum cost of the next one or two steps.
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])

        # 3. You can start from index 0 or 1, so answer is min(cost[0], cost[1])
        return min(cost[0], cost[1])

        '''
        Dry Run Example:
        Input: cost = [10, 15, 20]
        After append: cost = [10, 15, 20, 0]
        Loop from i = 1 to i = 0 (since len(cost) = 4)

        i = 1:
            cost[1] += min(cost[2], cost[3])
            cost[1] = 15 + min(20, 0) = 15 + 0 = 15

        i = 0:
            cost[0] += min(cost[1], cost[2])
            cost[0] = 10 + min(15, 20) = 10 + 15 = 25

        So final cost = [25, 15, 20, 0]
        Return min(cost[0], cost[1]) => min(25, 15) = 15

        Output: 15

        Time Complexity:
        - O(n), where n is the length of the cost array (we loop once from end to start).

        Space Complexity:
        - O(1) extra, since we modify the input array in-place (except for appending one value).

        Interview Notes:
        - This is a bottom-up DP solution in-place.
        - The array is modified to keep the min cost to "reach the top" from each index.
        - Appending 0 at the end makes edge handling easier.
        '''
