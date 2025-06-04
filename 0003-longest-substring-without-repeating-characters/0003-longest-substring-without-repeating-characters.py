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
