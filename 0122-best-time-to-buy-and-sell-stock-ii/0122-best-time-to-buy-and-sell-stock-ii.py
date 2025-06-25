class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0           #to cal the max profit

        for i in range(1, len(prices)): #iterate from 1 to last pt, start from 1 cause on the 0 day it will be -ve
            if prices[i] > prices[i-1]: #if the price is higher than the prev day
                maxprofit += prices[i] - prices[i - 1]  #store the price in max and cal the profit bet 2 days
        return maxprofit                #return the maxprofit

        #Time Complexity: O(n)
        #Space Complexity: O(1)