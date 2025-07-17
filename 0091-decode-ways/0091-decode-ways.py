class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i]: Number of ways to decode s[i:]
        dp = {len(s): 1}  # Base case: an empty string has one way to decode

        # Iterate backwards through the string
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                # No valid decode starts with '0'
                dp[i] = 0
            else:
                # At least as many ways as skipping one digit
                dp[i] = dp[i + 1]

            # Check if two-digit decode is valid (10-26)
            if (
                i + 1 < len(s)
                and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456"))
            ):
                # Add ways by skipping two digits
                dp[i] += dp[i + 2]
        return dp[0]

'''
--- Implementation Steps ---
1. Create a DP table (dictionary) with the base case: dp[len(s)] = 1 (empty string).
2. Loop i from len(s)-1 down to 0 (right to left):
    a. If s[i] == '0', set dp[i] = 0 (can't decode a message starting with '0').
    b. Otherwise, set dp[i] = dp[i+1] (decode one character).
    c. If a valid two-character decode is possible (i.e., 10-26), add dp[i+2].
3. At the end, return dp[0] (number of ways to decode the full string).

--- Dry Run ---
s = "226"
i = 2: s[2] = "6"
    - s[2] != '0' ⇒ dp[2] = dp[3] (which is 1, base case)
i = 1: s[1] = "2"
    - s[1] != '0' ⇒ dp[1] = dp[2]
    - s[1:3] = "26" (valid two-digit) ⇒ dp[1] += dp[3]
i = 0: s[0] = "2"
    - s[0] != '0' ⇒ dp[0] = dp[1]
    - s[0:2] = "22" (valid two-digit) ⇒ dp[0] += dp[2]
Final result: dp[0] = 3 (ZZF, BZF, BBF)

--- Time Complexity ---
O(n) - Single pass through the string.

--- Space Complexity ---
O(n) - dp dictionary has at most n+1 keys (one per position).

--- Interview Commentary ---
- "This is a bottom-up dynamic programming solution."
- "For each position, I check if I can decode 1 or 2 characters."
- "I use a dictionary for O(1) lookups, and process from right to left."
- "If s[i] is '0', it can't be decoded as a letter, so I set that path to 0."
- "If two-character decode is valid (10-26), I add those ways as well."
'''
