class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""                        #Empty string

        for i in range(len(strs[0])):   #Start with first string str[0], loop through each character index
            for s in strs:              #For every other string
                # First character with the first string strs0 with the first index
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res +=strs[0][i]            #If all strings matched char at position i, add that char to the res prefix
        return res                      #Return the result

#if i == len(s):
#That means the current string is shorter than index i, so common prefix can’t go beyond this.

#or s[i] != strs[0][i]:
#If any character at position i doesn't match strs[0][i], it breaks the prefix.

#Time Complexity: O(n*m)
#Space Complexity:O(1)