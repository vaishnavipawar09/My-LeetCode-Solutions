class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1                       #Left ptr but min k can be 1 so
        r = max(piles)              #right ptr but it can be max pile of banana koko can eat 
        res = r                     #If that is the max, she can eat all bananas, so store res with the max

        while(l<=r):                #Loop through the whole pile
            k = (l + r) // 2        #Cal the k value(mid value)

            totaltime= 0            #Total time taken for her to eat
            for i in piles:
                totaltime += math.ceil(float(i)/ k)        #Cal total time taken(cal hr for given k )
                                                    #Use math.ceil() or do manual ceiling: (pile + k - 1) // k
            if totaltime <= h:                   #if time is taken to eat banana is less than the h hours
                res = k                             #store the min k in result
                r = k - 1                           #if she cn eat the banana, try smaller speed
            else:                                   #else try the faster speed
                l = k + 1
        return res                                  #return the result

        #Time Complexity: O(n.log m)
        #Space Complexity: O(1)
