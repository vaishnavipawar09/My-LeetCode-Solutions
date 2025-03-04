"""class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        rev=0
        pal = x
        while x !=0:
            lastdigit = x % 10
            rev = rev * 10 + lastdigit
            x = x // 10
        return pal == rev"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False 
            
        org = x
        rev = 0
        while x != 0:
            rem = x % 10
            rev = rev * 10 + rem 
            x = x // 10
        
        return org == rev

       


        