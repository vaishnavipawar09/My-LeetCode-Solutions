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


"""
1. Clarifying Questions
Should I check for palindromicity after deleting at most one character? (Yes)
Is input guaranteed to be lowercase letters only? (Yes, per constraints)
What if the string is already a palindrome? (Return True)
What if multiple deletes are needed? (Only one delete allowed. If not possible in one, return False.)
Empty string? (Not possible per constraints.)

2. Test Cases
"aba" → True (already a palindrome)
"abca" → True (delete ‘c’ → “aba” or delete ‘b’/’a’ → not a palindrome)
"abc" → False (need to remove more than one)
"a" → True (single char is always palindrome)
"deeee" → True (delete 'd')

3. Approach
Use two pointers (left, right). Compare characters inward.
If mismatch:
Try deleting either s[left] or s[right] (skip that char) and check if the remaining substring is palindrome.
If either is a palindrome after one deletion, return True.
If no mismatches (or only one deletion needed), return True.

5. Edge Cases
No mismatches: return True.

First mismatch is at ends: try deleting from either end.

More than one mismatch after a single delete: return False.

6. Time & Space Complexity
Time: O(n) (Each character is checked at most twice)
Space: O(1) (No extra space used except for recursion stack, but that’s at most O(n) in rare case of very unbalanced string; usually iterative in helper.) """