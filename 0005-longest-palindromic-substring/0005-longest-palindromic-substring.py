class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Initialize the starting index and max length of result substring
        resIdx = 0
        resLen = 0

        # Loop over each character in the string to consider it as a potential center
        for i in range(len(s)):
            # --- Check for odd-length palindromes (single center) ---
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # If this palindrome is longer than current result, update result
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

            # --- Check for even-length palindromes (double center) ---
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

        # Return the substring that is the longest palindrome
        return s[resIdx : resIdx + resLen]

        '''
        --- Implementation Steps ---
        1. Initialize variables to track the starting index and max length of the result substring.
        2. For every index in the string, treat it as the center of a potential palindrome.
        3. Expand outwards to check for the longest odd-length palindrome.
        4. Expand outwards to check for the longest even-length palindrome.
        5. Each time you find a palindrome longer than the current best, update the start index and length.
        6. After processing all centers, return the longest palindrome substring found.

        --- Dry Run ---
        s = "babad"
        i = 0:
            Odd: l=r=0 ("b"), updates resIdx=0, resLen=1
            Even: l=0, r=1 ("ba") -- not a palindrome
        i = 1:
            Odd: l=r=1 ("a"), resLen=1. Expand to l=0, r=2 ("bab") - palindrome, updates resIdx=0, resLen=3
            Even: l=1, r=2 ("ab") -- not a palindrome
        i = 2:
            Odd: l=r=2 ("b"), resLen=3. Expand to l=1, r=3 ("aba") - palindrome, but same length as current, no update.
            Even: l=2, r=3 ("ba") -- not a palindrome
        i = 3:
            Odd: l=r=3 ("a"), resLen=3. Expand to l=2, r=4 ("ada") - palindrome, but not longer.
            Even: l=3, r=4 ("ad") -- not a palindrome
        i = 4:
            Odd: l=r=4 ("d"), no update.
            Even: l=4, r=5 (out of bounds)
        Final result: "bab" or "aba" (both valid, depends on which is found first).

        --- Time Complexity ---
        O(n^2), where n = len(s). For each center, expand outwards up to O(n).

        --- Space Complexity ---
        O(1) additional space (just integer variables).

        --- Interview Tips ---
        - Say out loud: "For each position, I expand outwards for both odd and even-length centers, updating the result if I find something longer."
        - This is called the "expand around center" approach.
        - There are faster algorithms (Manacher’s, O(n)), but this is optimal for coding interviews and easy to explain.
        '''
