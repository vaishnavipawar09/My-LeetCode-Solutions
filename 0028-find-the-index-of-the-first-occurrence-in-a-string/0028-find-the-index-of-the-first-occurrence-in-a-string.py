class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
        

#Range only until the needle, and comapre the haystack has the needle in it by comparison and the needle lrngth , if matches return 1, else return -1

#Time Complexity : O(n) because we check each possible starting index in haystack once
#Space Complexity : O(1) not using any extra space