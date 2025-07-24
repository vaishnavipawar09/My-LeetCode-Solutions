#Method 1: Two pointers sliding window (set = for loop) no if else condition
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()                 # Track unique chars in window
        l = 0                           # Left pointer
        res = 0                         # Max length result

        for r in range(len(s)):         # Right pointer expands using for-loop  O(n)
            while s[r] in charSet:      # If duplicate found, shrink from left  O(n)
                charSet.remove(s[l])                                           #O(1)
                l += 1
            charSet.add(s[r])           # Add current char                     #O(1)
            res = max(res, r - l + 1)   # Update max length

        return res

#Time Complexity: O(n) = O(n) +O(n)
#Space Compleity: O(k), k is size of unique characters

#Dry Run:
# abcabcbb
# l = 0, r -0, charset = [] = [a], res = 1
# l = 0, r = 1, charset = [a, b], res = 2
# l = 0, r = 2, charset = [a,b, c] res = 3
# l = 0, r= 3, charset = [a, b, c], a in the set charset = [b, c] l = 1,set = [b, c, a] res = max(3, 3- 1+1 )= 3
# l = 1, r = 4, charset = [b, c, a], b in set = [a, c], l = 2, set =[c, a, b], res =(3, 3) = 3
# l = 2, r = 5, char == [c, a, b] c in set = [a, b] l = 3, set =[a, b, c], res = (3, 3) = 3
# l = 3, r = 6, char = [a, b, c] b in set [a, c], l = 4, set = [a, b, c] res = (3, 3) = 3
# l =4, r = 7, char = [a, b, c] b in set [a, c] l = 5 set = [a, b, c], res = 3
# loop ends
# result = 3

"""
Clarifying Questions
Is the input always a string of ASCII characters?
Yes, includes English letters, digits, symbols, spaces.
What should I return if the string is empty?
Return 0.
Can I use extra space (like a set or map)?
Yes, extra space is allowed.

Edge Cases
Empty string "" → returns 0
All duplicates "aaaa" → returns 1
All unique "abcdef" → returns 6

One-liner to Remember
Sliding window with hash map to track last indices—move left pointer when you hit a duplicate.
"""
"""
Method 2: Optimal Hashmap solution 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}                          # Store char and its latest index
        l = 0                            # Left pointer
        res = 0                          # Max length

        for r in range(len(s)):
            if s[r] in mp:
                # Jump left to 1 position right of last occurrence
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r                # Update last seen index
            res = max(res, r - l + 1)   # Update max length

        return res
        
#Time Complexity: O(n)
#Space Compleity: O(k), k is size of unique characters

"""

"""
Method 3: Basic Implementation, that i thought of 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l , r = 0, 0                        #Initialize two pointers
        char = set()                        #Store char in a set    
        maxlen = 0                          #Cal max length of char

        while r < len(s):                   #Right ptr runs throough whole string
            if s[r] not in char:            #If not in char, add, wnique char
                char.add(s[r])              #Add new char to set
                r += 1                      #Move r forward
                maxlen = max(maxlen, r - l) #Update max len, when new char is added
            else:                           #If duplicate
                char.remove(s[l])           #Remove the leftmost character
                l += 1                      #Increment l
        return maxlen                       #Return max length of substring

#Time Complexity: O(n)
#Space Compleity: O(k), k is size of character set, unique characters

"""
