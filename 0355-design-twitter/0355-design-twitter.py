class Twitter:
    def __init__(self):
        self.count = 0                      #keep track of count (time)
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds] map each user to the tweets
        self.followMap = defaultdict(set)  # userId -> set of followeeId, map to check follow/unfollow

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])     #in the tweet map of user, add the tweetid but also add the count(time)
        self.count -= 1                     #next tweet to create at different count so decrement

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []                            #ordered starting from the most recent tweets
        minHeap = []                        #minheap to figure which was recent

        self.followMap[userId].add(userId)          #the user follows themselves
        for followeeId in self.followMap[userId]:   #go through each user that  the follower follows in the map
            if followeeId in self.tweetMap:         #check if they have atleast one tweet        
                index = len(self.tweetMap[followeeId]) - 1  #last value of th list 
                count, tweetId = self.tweetMap[followeeId][index]   #add that to the minheap
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])        #puh the values in the heap

        while minHeap and len(res) < 10:            #while minheap not empty and less than 10 values
            count, tweetId, followeeId, index = heapq.heappop(minHeap)      #pop these values
            res.append(tweetId)                     #add it to result
            if index >= 0:                          #assume that the index is valid
                count, tweetId = self.tweetMap[followeeId][index]   #tells  us the next tweet to add to min heap
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])    #push in the heap
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)          #from map, the follower is following the followee id, so add it in map 

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:        #if the follower is folllowing then only remove it 
            self.followMap[followerId].remove(followeeId)   #to unfollow remove the followwee id from the map of the follower


#Time Complexity: O(1) for other functionc, O(nlogn) for getNewsFeed
#Space Complexity: O(N * m + N * M + n)
#Space: O(U + totalTweets + totalFollows)
  # U = number of users
  # totalTweets = total number of tweets ever posted
  # totalFollows = total number of follow relationships (sum over all users)
