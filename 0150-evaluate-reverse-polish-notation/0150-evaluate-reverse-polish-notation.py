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

        return stack[-1]  # Final result on top of the stack
