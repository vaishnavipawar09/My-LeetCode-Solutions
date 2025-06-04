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


"""
Method 2: Two pointers sliding window (set = for loop) no if else condition
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()                 # Track unique chars in window
        l = 0                           # Left pointer
        res = 0                         # Max length result

        for r in range(len(s)):         # Right pointer expands using for-loop
            while s[r] in charSet:      # If duplicate found, shrink from left
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])           # Add current char
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
