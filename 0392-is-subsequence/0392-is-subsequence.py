class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0                           #Set the two ptrs of the two strings
        while i < len(s) and j < len(t):    #loops run through when i and j are less than the length of s and t 
            if s[i] == t[j]:                #If both the charcters are same, 
                i += 1                      #Now shift the i ptr to next position
            j += 1                          #Shift the j ptr too, cause we cant reuse the j char, if we dont find, only increase j
        return i == len(s)                  #Condition to return True, for every char in str s we found it in t

#Time Complexity: O(n)
#Space Complexity: O(1)

#Once i reaches out of bound we are done with the while loop
#Also given s is not a subsequence of t