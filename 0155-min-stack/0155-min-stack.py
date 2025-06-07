class MinStack:

    def __init__(self):
        self.stack = []                 #create a stack
        self.minstack = []              #create a stack to store the min values
        

    def push(self, val: int) -> None:
        self.stack.append(val)          #add the val in the stack
        val = min(val, self.minstack[-1] if self.minstack else val) #calculate the min. value
        self.minstack.append(val)       #add the minimum value in the minstack
        

    def pop(self) -> None:              #When you pop, make sure you pop from both the stacks, to keep it constant
        self.stack.pop()            
        self.minstack.pop()
        

    def top(self) -> int:               #returns up the top value of the stack
        return self.stack[-1]
        
    def getMin(self) -> int:            #returns the top value of minstack: stores the min. value
        return self.minstack[-1]        
        

#Time Complexity: O(1) for all operations
#Space Complexity: O(n) 

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()