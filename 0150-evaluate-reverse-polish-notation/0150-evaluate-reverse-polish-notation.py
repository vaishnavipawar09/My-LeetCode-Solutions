class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  # Stack to store operands
        operators = {'+', '-', '*', '/'}  # Set of valid operators

        for c in tokens:
            if c in operators:
                val2 = stack.pop()  # Second operand
                val1 = stack.pop()  # First operand

                # Perform the operation based on the operator
                if c == '+':
                    result = val1 + val2
                elif c == '-':
                    result = val1 - val2
                elif c == '*':
                    result = val1 * val2
                elif c == '/':
                    result = int(val1 / val2)  # Truncate toward zero

                stack.append(result)  # Push result back to the stack
            else:
                stack.append(int(c))  # Push number to stack

        return stack[0]  # Final result 

#Time Complexity: O(n)
#Space Complexity: O(n)

"""
#Both have same time and space complexity , the beow one is a bi more efficient cause less lines of code
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  # Stack to hold operands

        for c in tokens:
            if c == "+":
                # Add top two numbers and push result
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                # Pop two numbers and subtract in correct order
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                # Multiply top two numbers and push result
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                # Pop two numbers and divide in correct order
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))  # Truncate toward zero
            else:
                # Convert and push operand
                stack.append(int(c))

        return stack[0]  # Final result

"""