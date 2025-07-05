class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
#Convert stones to negatives, Now largest stone will always be at “smallest” end of the min-heap (because it’s the most negative).
        stones = [-s for s in stones]  
        heapq.heapify(stones)                   #create a maxheap
        
        while len(stones) > 1:                  #cause we want only last remaining element in the heap
            first = heapq.heappop(stones)       #pop both elements cause they are the largest now
            second = heapq.heappop(stones)
            if second > first:                  #first should be greater but in case second is greater, it has new weight 
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])


        