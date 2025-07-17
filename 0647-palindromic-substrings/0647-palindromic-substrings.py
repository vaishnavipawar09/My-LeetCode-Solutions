class Solution:
    
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res += self.countPali(s, i, i)          #here passed the left and right ptr for odd that is i, i    
            res += self.countPali(s, i, i + 1)      #here passed the left and right ptr for eventhat is i, i +1   
        return res

    def countPali(self, s, l, r):           #Same as below code, just created a helper function the reduce the lies of the code
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res
       
       
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        # Initialize the result counter
        res = 0

        # For each character and each gap between characters (odd & even centers)
        for i in range(len(s)):
            # Odd-length palindromes: expand around a single character
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1      # Found a palindromic substring
                l -= 1
                r += 1

            # Even-length palindromes: expand around the gap between characters
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res

        '''
        --- Implementation Steps ---
        1. Initialize a result counter (res) to 0.
        2. For each index in s:
            a. Expand outwards from s[i] for odd-length palindromes.
            b. Expand outwards from between s[i] and s[i+1] for even-length palindromes.
            c. Every time the substring is a palindrome, increment res.
        3. Return res as the number of palindromic substrings.

        --- Dry Run ---
        s = "aaa"
        i = 0: Odd: "a" (res=1), Even: "aa" (res=2)
        i = 1: Odd: "a" (res=3), Expand: "aaa" (res=4), Even: "aa" (res=5)
        i = 2: Odd: "a" (res=6)
        Total: 6 palindromic substrings

        --- Time Complexity ---
        O(n²), since for each center you may expand up to n times.

        --- Space Complexity ---
        O(1), just counters and loop variables.

        --- Interview Guidance ---
        - "I'm using expand-around-center to check every possible palindrome."
        - "For each position (and each gap), I grow outwards, and count palindromes."
        - "Single letters, two letters, and longer substrings are all handled."
        '''
"""