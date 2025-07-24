#Optimal Solution: Used only maxf
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0                         # Left pointer
        maxf = 0                      # Max frequency of a single char in window
        count = {}                    # Frequency map
        res = 0                       # Track max window length

        for r in range(len(s)):       # Expand window
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])  # Only update max of the current char

            # Shrink window if replacements needed > k
            while (r - l + 1) - maxf > k:  #Here (r - l + 1) is the window size
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1) # Update max length of valid window
        return res

#Time Complexity: O(n)
#Space Complexity : O(m) , m is unique characters

#Dry Run
#ABAB
# l = 0, r = 0, count= [] mf = 0, count = [A: 1], mf = 1, res = (0, 1) = 1
# l = 0, r = 1, count = [A: 1, B: 1] mf = 2  (1-0 + 1) = 2-2 0 <= k, res = (1, 1-0+1) = 1
# l = 0, r = 2, count = [A: 2, B:1] mf = 2 (2-0+1) - 2 <= k, (3-2= 1) 1<=k , res = (1, 2-0+1) = (1, 3) = 3
# l = 0, r = 3, count = [A:2, B:2] mf = 2 (3-0 +1)= 4-2 <=k, valid res (3, 3-0+1) = (3, 4) = 4
# res = 4
"""
Method: Main code to understand completely : O(26. n)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0                         # Left pointer of the sliding window
        count = {}                    # Store frequency of characters in window
        res = 0                       # Store max window size (final answer)

        for r in range(len(s)):       # Expand window by moving right pointer
            count[s[r]] = 1 + count.get(s[r], 0)

            # If too many characters need to be replaced (> k), shrink window
            while (r - l + 1) - max(count.values()) > k:  #Here (r - l + 1) is the window size
                count[s[l]] -= 1      # Shrink from left
                l += 1

            res = max(res, r - l + 1) # Update result if window is valid
        return res

Time Complexity: O(26.n)
Space Complexity : O(m) , m is unique characters
    
"""