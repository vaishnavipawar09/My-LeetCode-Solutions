class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)] #Create array of pairs, use zip to create the pairs together(list comprehension)
        pair.sort(reverse=True)     #Sort the array, in reverse order
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)      #Calculate time, add it to stack, = dist/speed, willl give a decimal
            if len(stack) >= 2 and stack[-1] <= stack[-2]: #if one car no need to do anything, but two car, there might be collision
                stack.pop()     #If possibility to collide, pop the car
        return len(stack)       #return stack

        #Time Complexity: O(n logn)
        #Space Complexity: O(n)