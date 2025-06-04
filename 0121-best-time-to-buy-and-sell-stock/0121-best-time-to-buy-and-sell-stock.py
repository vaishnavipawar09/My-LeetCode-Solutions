class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP
        
        """
        My version that I solved: Greedy approach:
        minprice = prices[0]  # Set the first price as the lowest seen so far (temp value to track min)
        maxprofit = 0         # Create a variable to store max profit found so far

        for i in range(len(prices)):  # Go through the entire price list
            if prices[i] < minprice:
                minprice = prices[i]  # If we find a new lower price, update the minprice
            else:
                profit = prices[i] - minprice  # If price is higher, calculate profit if we sold here
                if profit > maxprofit:
                    maxprofit = profit  # Only update max profit if the new one is greater

        return maxprofit  # Return the best profit found

        #Time Complexity: O(n)
        #Space Complexity: O(1)

        """
