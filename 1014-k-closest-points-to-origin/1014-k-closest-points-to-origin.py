class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []            # min heap a list

        for x, y in points:     #loop through the points
            dist = (x ** 2) + (y ** 2)  #cal the dis, we dont need to find the sqrt here
            minheap.append([dist, x, y])#append the dist and the points in the heap


        heapq.heapify(minheap)  #create the min heap now
        res = [ ]               #list for the result
        while k > 0:            #when k > 0 , pop through the heap and append it to the res
            dist, x, y = heapq.heappop(minheap)     #pop 3 values
            res.append([x, y])  #append only the points
            k -=1               #decrement k

        return res              #return the solution
        

        #Time Complexity: O(k * log n)
        #Space Complexity: O(n)