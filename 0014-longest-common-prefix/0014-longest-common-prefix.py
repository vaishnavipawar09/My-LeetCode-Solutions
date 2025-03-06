class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                # First character with the first string strs0 with the first index
                if i == len(s) or s[i] != strs[0][i]: 
                    return res
            res +=strs[0][i]
        return res