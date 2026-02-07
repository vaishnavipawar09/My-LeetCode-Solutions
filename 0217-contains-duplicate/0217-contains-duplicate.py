class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()         #Create a hashset for easy lookups
        for i in nums:          #for i in the list nums
            if i in hashset:    #Check if that int value exists in the hashset, if yes return True
                return True     
            hashset.add(i)      #After the check, make sure to add the int in the hashset
        return False            #After the loop ends, no duplicate, then return False

#Time Complexity: O(n), iterating once and doing O(1) average lookups in a set. 
#Space Complexity: O(n), worst case in case all the values need to be stored in hashset 

#Dry Run
# nums = [1, 2, 3, 1]  hashset = {}
# Step 1 : i = 1, 1 not in hashset, so add hashset = {1}
# Step 2 : i = 2, 2 not in hashset, so add, hashset = {1, 2}
# Step 3 : i = 3, 3 not in hashset, so add, hashset = {1, 2, 3}
# Step 4 : i = 1, 1 is there in hashset, so return True

#Pattern to Remember: “Seen Before” / Duplicate Detection
# Use a set when: 
# 1. You need to know if something appeared earlier
# 2. Order doesn’t matter
# 3. Fast lookup is required