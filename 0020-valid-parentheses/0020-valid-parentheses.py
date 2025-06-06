class Solution:
    def isValid(self, s: str) -> bool:
        stack = []                  #STack with python list
        #Map all closing bracket with its opening brackets
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:                 #Go through all the char in the input string 
            if c in closeToOpen:    #If char is closing parathesis, 
                #so make sure stack is not empty and value of the top of stack the opening matching paraenthesis
                if stack and stack[-1] == closeToOpen[c]:   #Stack[-1] is the top of stack
                    stack.pop()     #Pop from stack if match
                else:
                    return False    #No match or empty 
            else:
                stack.append(c)     #If we get open parenthesis in start add it to the stack
        
        return True if not stack else False #Stack is empty(no unmatched brackets remain) return true else false

        #Time Complexity : O(n)
        #Space Complexity : O(n)