class KthLargest:
    import heapq

    def __init__(self, k: int, nums: List[int]):
        self.k = k                          #initialize k to k
        self.heap = nums                    #initialize minheap to nums
        heapq.heapify(self.heap)            #create the heap 
        while len(self.heap) > k:           #If heap goes over the fixed limit of k
            heapq.heappop(self.heap)        #pop the smallest value, which will be on top/last
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)      #add the value in the heap
        if len(self.heap) > self.k:         #If heap goes over the fixed limit of k
            heapq.heappop(self.heap)        #pop the smallest value, which will be on top/last
        return self.heap[0]                 #Return first element which will be the largest val in a min heap

#Time Complexity: O(m * log k)  m = no. of calls made to add()
# add funt is log n, initialization funt is n so basically O(n log n)
#Space Complexity: O(k)         min heap of size k , cause we need the kth largest element

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)