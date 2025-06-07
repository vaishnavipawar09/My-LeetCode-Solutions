class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []      #Use stack
        res = []        #To store result

        #Function for backtrack, using recursion
        def backtrack(openN, closedN):
            if openN == closedN == n: #If the num of open and close brackets are same
                res.append("".join(stack))  #add it to the result stack
                return

            if openN < n:               #add open then check if open < n
                stack.append("(")       #add the open parenthesis to the stack
                backtrack(openN + 1, closedN)   #while backtrack increment open
                stack.pop()

            if closedN < openN:         #To add a closed parenthesis
                stack.append(")")
                backtrack(openN, closedN + 1)   #increment the close bracket counter
                stack.pop()              #update the stak by popping

            
        backtrack(0, 0)                 #intial opening and closed count
        return res

        