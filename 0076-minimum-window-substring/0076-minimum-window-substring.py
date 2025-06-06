class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0                       #Left ptr
        counts, countt = {}, {}     #Hashmap for s and t     
        have = 0                    #we need 0 char for now
        res = ""                    #res
        resLen = float("infinity")       #len of result

        if t == "":
            return ""               #return empty if the string is empty

        # Step 1: Build the target count map of t, add the char to the map 
        for c in t:
            countt[c] = 1 + countt.get(c, 0)
        need = len(countt)          #total str of t which is needed

        # Step 2: Sliding window
        for r in range(len(s)):     #iterate through s string using r ptr
            counts[s[r]] = 1 + counts.get(s[r], 0)  #Add char of s in the hashmap

            # If current char satisfies one needed char
            if s[r] in countt and counts[s[r]] == countt[s[r]]:
                have += 1           #Update the have cnt if cond satisfied

            # Shrink the window as long as all chars are satisfied
            while have == need:
                # Update result if smaller window found
                if (r - l + 1) < resLen: #r - l + 1 is the window 
                    res = s[l:r + 1]    
                    resLen = r - l + 1  #len of res is the size of the window

                # Shrink from the left
                counts[s[l]] -= 1       #Remove left most char
                if s[l] in countt and counts[s[l]] < countt[s[l]]: #If it is one of the char e need and if the count is                                                                 less than actual count the need
                    have -= 1           #Remove from have count 
                l += 1                  #increment by 1

        return res if resLen != float("infinity") else ""

#Time Complexity : O(n + m), n = len(t), m = len(s)
#Space Complexity: O(1)