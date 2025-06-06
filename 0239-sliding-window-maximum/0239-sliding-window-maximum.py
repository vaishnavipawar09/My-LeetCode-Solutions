class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = r = 0                               #Two pointers
        q = deque()                             #deque
        res= []                                 #result         

        while r < len(nums):                    #while r is still in bound
            while q and nums[q[-1]] < nums[r]:  #check if empty and no smaller values exist in the queue
                q.pop()                         #remove values if that cond is true
            q.append(r)                         #add value r in deque

            if l > q[0]:                        #remove left value, if left index is greater than the right value
                q.popleft()                     #used popleft to pop left value from the window

            if (r + 1) >= k:                    #check if window is atleast size k 
                res.append(nums[q[0]])          #added it to the result for max 
                l+=1                            #increment left 
            r += 1                              #move the window, increment r
        
        return res                              #return the max sliding window

#Time Complexity: O(n)
#Space Complexity: O(n)
        