class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequency of each number
        hashmap = {}
        for num in nums:            #for each num in the array check if exists in hashmap
            if num in hashmap:      #if yes, increase the value of it 
                hashmap[num] += 1
            else:                   #if no, it is new, add it into hashmap
                hashmap[num] = 1

        # Step 2: Create buckets where index = frequency
        freq = [[] for _ in range(len(nums) + 1)]

        # Step 3: Fill the buckets
        for num, count in hashmap.items():
            freq[count].append(num)

        # Step 4: Extract top k frequent elements
        res = []
        for i in range(len(freq) - 1, 0, -1):       #start the loop in backward direction high freq
            for num in freq[i]:                     #loop over nums, and add it to res
                res.append(num)
                if len(res) == k:                   #stop wen we acheve the top k elements
                    return res

#Time: O(n),    Count → O(n),   Fill buckets → O(n).    Scan buckets → O(n)
#Space: O(n)    Hashmap + buckets

#Dry Run:
# nums = [1,1,1,2,2,3], k = 2
# hashmap = { 1: 3, 2: 2, 3: 1}, freq[1] = 3, freq[2] = 2, freq[3] = 1
# res = [], start from last freq
# res = [1, 2]      res == k so stop
# Output : res = [1, 2]

#Pattern: Frequency Counting + Bucket Sort (by frequency)
#Use this when: 1. You need top K
# 2. Sorting is too slow
# 3. Frequencies are bounded by n