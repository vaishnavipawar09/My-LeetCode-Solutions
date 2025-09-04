class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #Create a hashset
        hashset = set()
        for n in nums:        #O(n) times
            if n in hashset:  #Check if n is a duplicate    O(1)
                return True   #Found Duplicate
            hashset.add(n)    #Add values to the hashset    O(1)
        return False          #No Duplicate

#Dry Run
#nums = [1, 2, 3, 1], hashset = {}
# 1. n = 1, hashset = {1}
# 2. n = 2, hashset= {1, 2}
# 3. n = 3, hashset = {1, 2, 3}
# 4. n = 1 yes exists, Output : true

#Time Complexity: O(n)
#Space Complexity : O(n)
