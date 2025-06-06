class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        counts, countt = {}, {}
        have = 0
        res = ""
        resLen = float("inf")

        if t == "":
            return ""

        # Step 1: Build the target count map
        for c in t:
            countt[c] = 1 + countt.get(c, 0)
        need = len(countt)

        # Step 2: Sliding window
        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)

            # If current char satisfies one needed char
            if s[r] in countt and counts[s[r]] == countt[s[r]]:
                have += 1

            # Shrink the window as long as all chars are satisfied
            while have == need:
                # Update result if smaller window found
                if (r - l + 1) < resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1

                # Shrink from the left
                counts[s[l]] -= 1
                if s[l] in countt and counts[s[l]] < countt[s[l]]:
                    have -= 1
                l += 1

        return res if resLen != float("infinity") else ""

#Time Complexity : O(n + m), n = len(t), m = len(s)
#Space Complexity: O(1)