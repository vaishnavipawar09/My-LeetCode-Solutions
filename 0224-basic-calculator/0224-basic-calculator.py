#Clarifying questions:
#Is the input always a string ? should  the output always be an integer or can it be float?
#Characters alllowed: + - * / ( )
#Should i ignore all the spaces? yes
# -(-1) that is 1 handle that ? unary minus 
#Are () are they always valid and balanced? 
# Can i assume the results always fit in 32 bit integer? yes

#(1 +(5 +4+2) -3) +(6 + 8)  -> 1 + 11 -3 + 14 -> 12 -3 + 14 -> 23

#Stack to handle the paranthesis
#result, sign
#approach: ignore spaces, if digit build the current number 
#if + add last num to res, sign +1
# if - add the last num to res , set the sign to -1
# ( push res and sign to stack, rese the res and sign
# ) pop sign res and combine them
# end don't forget to add last number to the result 




class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        sign = 1  # =ve , -ve -1
        num = 0


        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)  # multi digit 
            elif char == '+':
                res += sign * num          # Add previous number with its sign
                sign = 1                   # Next sign is +
                num = 0                    # Reset number
            elif char == '-':
                res += sign * num
                sign = -1
                num = 0
            elif char == '(':
                # Push current result and sign for later
                stack.append(res)
                stack.append(sign)
                res = 0                    # New sub-result inside ()
                sign = 1                   # Default sign inside ()
            elif char == ')':
                res += sign * num          # Finish the inner expression
                res *= stack.pop()         # Multiply by sign before '('
                res += stack.pop()         # Add to result before '('
                num = 0

        res += sign * num
        return res

        