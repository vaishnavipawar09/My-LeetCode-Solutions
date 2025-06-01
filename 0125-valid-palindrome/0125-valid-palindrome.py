class Solution:
    def isPalindrome(self, s: str) -> bool:
        l , r =0, len(s) - 1        #Create a Two pointers
        while l< r:                 #Iterate through the string
        #In python, wanna call another function, inside a object use the self keyword.
            while l< r and not self.alphaNumeric(s[l]): #If left is not alphanumeric, increment the left pointer
                l+=1                #increment left pointer
            while l< r and not self.alphaNumeric(s[r]): #If right is not alphanumeric, decrement the right pointer
                r-=1                #decrement right pointer

            if s[l].lower() != s[r].lower():    #If not equal return false
                return False
             
            l, r= l+1, r-1          #Update the left and right pointers for comparison
        return True                 #String is a palindrome


#get ASCII value of character using ord function
#Create a function for checking it is alphanumeric 
    def alphaNumeric(self, c):        
        return (ord('A')<= ord(c)<= ord('Z') or
                    ord('a')<= ord(c)<= ord('z') or 
                    ord('0')<= ord(c)<= ord('9'))

  #Time Complexity: O(n)
  #space complexity : O(1)

"""
Solution 1: Uses a lot of functions, and we use extra memory 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = "                          #Create a new str

        for c in s:
            if c.isalnum():                 #Convert to alpha numeric
                newstr += c.lower()         #convert to lower case and add
        return newstr == newstr[::-1]       #return true if reverse str 

        Time and space complexity : O(n)
"""
