class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

#My solution:
        if len(s) != len(t):                   #Handle the edge case, if len of strings dont match return False
            return False
        
        hashmap = dict()                        #Create a key value pair hashmap
        for i in s:                      #O(n)  #for the char in s, if it exists in hashmap, add and increase the count
            if i in hashmap:
                hashmap[i] = hashmap[i] + 1
            else:                               #else keep the char count to 1
                hashmap[i] = 1
      
        for j in t:                     #O(n)   #for the char in t, if it exists in hashmap, remove and decrease the count 
            if j in hashmap:
                hashmap[j] = hashmap[j] - 1
                if hashmap[j] < 0:              #Edge case in case the hashmap value goes beyond 0
                    return False
            else:
                return False                    #If the char is not in hashmap or a new char, immediately return False
        return True                             #If all char, key value pair satisfied then return true, they are a match


#Time Complexity: O(n)
#O(n) two for loops, so O(n) + O(n) = O(n), other if statement is O(1)
#Space Complexity: O(1) 
#For Unicode characters, space becomes O(k), where k is the number of unique characters.

#Dry Run:
#s = "rat", t = "car"
# After 1st for loop the hashmap = {a: 1, r:1, t:1}
# j = c not in hashmap, so else statement return false


#Pattern: Frequency Map (Count → Consume) Pattern
#Use when:
# 1. Order doesn’t matter
# 2. Frequency matters
# 3. You want early failure detection

#Neetcode Solution:
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
        """




        