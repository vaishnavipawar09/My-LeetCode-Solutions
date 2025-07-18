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


        #Time Complexity: O(n)
        #Space Complexity: O(n)


#Dry Run: (1 +(5 +4+2) -3) +(6 + 8)
# stack = [], res = 0 sign = 1, num =0
# (  stack = [0, 1] res = 0, sign =1
# 1 num = 1 sign = 1, res = 0
# + res = 1, sign = 1, num  =0 
# ( stack = [0, 1, 1, 1], res = 0, sign = 1
# 5 num = 5 , sign = 1, res = 0
# + res = 5 * 1= 5 , sign = 1, num = 0
# 4 num = 4, sign = 1, res = 5
# + res =res = 4, res = 5+4 = 9, sign = 1, num = 0
# 2 num = 2, sign = 1, res = 9
# ) res = 2 * 1 + res = 2 +9 = 11, pop sign (11 * sign -> 11 * 1), pop res ( 1 + 11) = 12 stack = [0, 1]
# - res = 12, num = 0, sign = -1
# 3 num = 3, sign = -1, res = 12
# ) res = num * sign + res -> res = 12 -3 = 9, pop sign (9 * 1) = 9 , pop res 0+9 = 9 
# + res = 9 + (0* 1) = 9, sign = 1, num = 0
# ( stack =[9, 1] res = 0, sign = 1
# 6 num = 6, sign = 1, res = 0
# + res = res +(sign * num) -> res = 0 +(1*6) -> 6
# 8 num = 8 , sign = 1, res = 6
# ) res = 6 + 8 = 14 , res = 14 * 1 = 14 , ree = 14 + 9 = 23


        