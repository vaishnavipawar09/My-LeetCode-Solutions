class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
#Convert stones to negatives, Now largest stone will always be at “smallest” end of the min-heap (because it’s the most negative).
        stones = [-s for s in stones]  
        heapq.heapify(stones)                   #create a maxheap

        while len(stones) > 1:                  #cause we want only at most one element in the heap
            first = heapq.heappop(stones)       #pop both elements cause they are the largest now
            second = heapq.heappop(stones)
            #here second will be greater cause we ae using the -ve of the values, eg f = -8 s =-7
            if second > first:                  #here second is smallest , so it gets destoryed and new weight 
                heapq.heappush(stones, first - second)

        stones.append(0)                #edge case: if nothing to return , add 0 at last so we return 0
        return abs(stones[0])           #return stone at index 0, also abs cause we need to return +ve value


#Time Complexity: O(n log n)
#Space Complexity: O(n)

        