class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # each task 1 unit time, and minimize idle time

        count = Counter(tasks)      #Create a counter to keep a count of freq of task
        
        # Use maxheap to always schedule the most frequent task first
        maxheap = [-cnt for cnt in count.values()]  #maxheap use -ve count cause python heap has minheap 
        heapq.heapify(maxheap)      #convrt the list to a heap, for valid heap structure
        
        #we will use a maxheap and a deque combination here
        time = 0                    #to cal the time taken
        q = deque()                 #create a deque which is pairs of [-cnt, idleTime]
        while maxheap or q:         #while maxheap and q are not empty
            time += 1               #increment the timer, cause each is of one count time

            if maxheap:         #ifMaxHeap is non empty
                cnt = 1 + heapq.heappop(maxheap) #pop from the heap and add it to cnt, add +1 cause they are -ve
                if cnt:             #if cnt is not empty
                    # Add this task to the cooldown queue, can't be scheduled again until time + n
                    q.append([cnt, time + n])   #append it in the deque, append cnt and time and n = 1
            
            # If there are tasks whose cooling time is up, re-add them to the heap for scheduling
            if q and q[0][1] == time:   #if q is not empty, first value in the queue is equal to time
                heapq.heappush(maxheap, q.popleft()[0]) #pop the pair of values, and care first value, add it to the heap
            # No need to handle the idle situation explicitly, time still increments for each loop

        return time     #return the time taken


#Time Complexity : O(m) , m = number of tasks 
#Pop Minimum O(log n) = O(log 26) = O(n)


#Space Complexity: O(1), at most 26 characters
