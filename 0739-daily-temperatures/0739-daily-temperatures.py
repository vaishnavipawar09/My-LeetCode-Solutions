class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)  # Pre-fill answer with 0s
        stack = []                        # Stack will hold indices pair: [temp, index]

        for i, t in enumerate(temperatures):    #Enumerate t make it easier
            # While stack is not empty AND current temp > temp at index on top of stack
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()  # stack temp and stack index
                answer[stackInd] = i - stackInd    # Days waited
            stack.append([t, i])  # Always push temp value and index
        return answer

#Time & Space Complexity: O(n)