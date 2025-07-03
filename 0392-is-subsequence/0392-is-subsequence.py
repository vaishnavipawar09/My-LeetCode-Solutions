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
#Also given s is a subsequence of t, and not the other way around

#We are iterating and increamenting the s str cause, once that is over we dnt have to check anything cause s is subsequence of t, and not the other way around

#DRY RUN
# s = abc, t = ahbgdc
# 1. i = j = 0, 0< 3 and 0< 6 yes, s[0] == t[0] -> a == a , yes, i = 1, j = 1
# 2. i = j = 1, 1<3, 1< 6, s[1] == t[1] -> b == h does not satisfy so j +1, j = 2
# 3. i = 1, j = 2, 1<3, 2< 6 , s[1] == t[2] -> b == b, yes, i=2, j = 3
# 4. i =2, j = 3, 2< 3, 3< 6, s[2] == t[3] ->g no, increment j , j =4
# 5. i = 2, j = 4. 2< 3, 4< 6, s[2] == t[4] -> c ==d, no , j = 5
# 6. i =2, j =5, 2< 3, 5<6, s[2] == t[5] -> c == c , yes, i = 3, j = 6
# 7. i = 3, j = 6 3 < 3 no end the while loop , return i == len(s)  3 ==3 yes, return True
#Output: True