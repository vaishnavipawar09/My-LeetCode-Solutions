#Optimal Solution:
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):  # s1 can't be a permutation of a shorter s2
            return False
        
        s1Count, s2Count = [0] * 26, [0] * 26  # frequency arrays for s1 and current window of s2

        # Initialize counts for the first window of s2 and full s1
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # Count how many characters match between s1 and s2 window
        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0  # Left pointer of the sliding window
        # Slide the window over s2 one character at a time
        for r in range(len(s1), len(s2)):
            if matches == 26:  # If all 26 characters match, we found a valid permutation
                return True

            # Include new character on the right into the window
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # Remove the character going out from the left of the window
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1

            l += 1  # Slide the window

        return matches == 26  # Final check for the last window

#Time Complexity: O(n)   , n is len of s2 string
#Space Complexity: O(1)

"""
My solution:

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False  # s1 cannot be a substring if it's longer than s2

        l = 0
        counts1 = {}  # Frequency map for s1
        counts2 = {}  # Frequency map for the current window in s2

        # Build frequency map for s1
        for c in s1:
            counts1[c] = 1 + counts1.get(c, 0)

        for r in range(len(s2)):
            # Add current character to window frequency map
            counts2[s2[r]] = 1 + counts2.get(s2[r], 0)

            # Shrink the window if it’s larger than s1
            while (r - l + 1) > len(s1):
                counts2[s2[l]] -= 1
                if counts2[s2[l]] == 0:
                    del counts2[s2[l]]  # Remove char with zero count for clean comparison
                l += 1

            # Compare the two frequency maps when the window size matches s1
            if counts1 == counts2:
                return True

        return False  # No valid permutation found

#Time Complexity: O(26.n)   , n is len of s2 string
#Space Complexity: O(1)

"""
