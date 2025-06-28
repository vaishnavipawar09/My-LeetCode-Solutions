#Here we iterate from the last of the array
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1                  #Start the ptr at the last of the array
        length = 0                      #cal the length of last word

        while s[i] == ' ':              #If there is space at the end before the word skip trailing spaces
            i -= 1                      #Decrement the ptr to find the where the word ends?

        while i >= 0 and s[i] != ' ':   #If i is at some word, and also if end of the string exit the loop, and char is not a space
            length += 1                 #Count the length of the last word
            i -= 1                      #Decrement the ptr to cal the length until you hit a space

        return length                   #return the length

            
#Time Complexity: O(n)
#Space Complexity: O(1)

        '''
        #Here we iterate from the start itself
        length = i = 0
        while i < len(s):
            if s[i] == ' ':
                while i < len(s) and s[i] == ' ':
                    i += 1
                if i == len(s):
                    return length
                length = 0
            else:
                length += 1
                i += 1
        return length
        '''