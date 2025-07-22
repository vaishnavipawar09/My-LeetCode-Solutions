class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_Palindrome(l, r):
            while l< r:              #Iterate through the string
        #In python, wanna call another function, inside a object use the self keyword.
                while l< r and not self.alphaNumeric(s[l]): #If left is not alphanumeric, increment the left pointer
                    l+=1                #increment left pointer
                while l< r and not self.alphaNumeric(s[r]): #If right is not alphanumeric, decrement the right pointer
                    r-=1                #decrement right pointer

                if s[l].lower() != s[r].lower():    #If not equal return false
                    return False
             
                l, r= l+1, r-1          #Update the left and right pointers for comparison
            return True 
                
        l , r =0, len(s) - 1        #Create a Two pointers
        while l< r:                 #Iterate through the string
        #In python, wanna call another function, inside a object use the self keyword.
            while l< r and not self.alphaNumeric(s[l]): #If left is not alphanumeric, increment the left pointer
                l+=1                #increment left pointer
            while l< r and not self.alphaNumeric(s[r]): #If right is not alphanumeric, decrement the right pointer
                r-=1                #decrement right pointer

            if s[l].lower() != s[r].lower():    #If not equal return false
                return is_Palindrome(l+1, r) or is_Palindrome(l, r-1)
             
            l, r= l+1, r-1          #Update the left and right pointers for comparison
        return True                 #String is a palindrome


#get ASCII value of character using ord function
#Create a function for checking it is alphanumeric 
    def alphaNumeric(self, c):        
        return (ord('A')<= ord(c)<= ord('Z') or
                    ord('a')<= ord(c)<= ord('z') or 
                    ord('0')<= ord(c)<= ord('9'))
