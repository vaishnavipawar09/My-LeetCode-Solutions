class Solution:
    def isPalindrome(self, s: str) -> bool:
        NewString=  ""

        for c in s:
            if c.isalnum():
                NewString += c.lower()
        return NewString == NewString[::-1]
        