class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      #My version that I solved: Greedy approach:
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

        #Time Complexity: O(n), loops only once
        #Space Complexity: O(1) , no extra memory needed

        """
        Method 2: Sliding window/ Two Pointers
        l, r = 0, 1                     # l = buying day, r = potential selling day
        maxP = 0                        # Track the max profit seen so far

        while r < len(prices):         # Loop until r reaches the end of the price list
            if prices[l] < prices[r]:  # If selling price is higher than buying price
                profit = prices[r] - prices[l]  # Calculate profit for this buy-sell pair
                maxP = max(maxP, profit)        # Update max profit if current one is better
            else:
                l = r                  # If current price is lower, treat it as new buying day
            r += 1                     # Move to next day (potential sell day)

        return maxP                    # Return the best profit found

        #Time Complexity: O(n)
        #Space Complexity: O(1)
        """

