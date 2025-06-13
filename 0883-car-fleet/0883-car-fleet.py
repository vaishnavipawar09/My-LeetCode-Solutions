class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #Create array of pairs, use zip to create the pairs together(list comprehension)
        pair = [(p, s) for p, s in zip(position, speed)] 
        pair.sort(reverse=True)     #Sort the array, in reverse order
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)      #Calculate time, add it to stack, = dist/speed, willl give a decimal
            #if one car no need to do anything, but two car, there might be collision
            if len(stack) >= 2 and stack[-1] <= stack[-2]: 
                stack.pop()     #If possibility to collide, pop the car
        return len(stack)       #return stack

        #Time Complexity: O(n logn)
        #Space Complexity: O(n)