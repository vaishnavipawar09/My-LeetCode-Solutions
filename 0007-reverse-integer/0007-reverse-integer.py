class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        neg = x<0
        x = abs(x)
        while x>0:
            lastdigit = x % 10
            rev=(rev * 10) + lastdigit
            x = x // 10
        if neg:
            rev = -rev

        if rev < -(2**31) or rev > (2**31 -1):
            return 0
        return rev