class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]
'''
#Optimal solution: Quick Select Algorithm
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k           #Target index we are looking for

        def quickSelect(l , r):     #pass left and right ptrs
            pivot, p = nums[r], l   #pivot is rigt most value, and p ptr is let most position
            for i in range(l, r):   #iterate through the array, r is non inclusive in pyton, so wont go or last val
                if nums[i]<= pivot: #to get partition, if val is less than the pivot
                    nums[p], nums[i] = nums[i], nums[p] #Swap p and i indexed nums
                    p += 1          #increment the ptr
            
            nums[p], nums[r] = nums[r], nums[p] #later swap the pivot value with the p index

            if p > k: return quickSelect(l , p - 1) #left subarray, left portion of partition array
            elif p < k: return quickSelect(p + 1, r)   #right subarray, this is if k> p, go right portion
            else: return nums[p]            #if both p and k are equal just return the pivot(nums[p])

        return quickSelect(0, len(nums) - 1) #call quickselect l = 0, r = len(nums) - 1


#Time Complexity: n  + n/2 + n/4 = O(2n) = Avg case = O(n), worst case = O(n^2)
#space Complexity : O(n)
'''       