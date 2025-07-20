class Solution:
    def numTrees(self, n: int) -> int:
        numTree = [1] * (n + 1)

        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                left = root - 1
                right = nodes - root
                total += numTree[left] * numTree[right]
            numTree[nodes] = total

        return numTree[n]
        
#Time & Space Complexity
#Time: O(n^2) (nested loops)
#Space: O(n) for the DP array

#Dry Run (n=3)
#G[0] = 1, G[1] = 1
#G[2] = G[0]G[1] + G[1]G[0] = 1*1 + 1*1 = 2
#G[3] = G[0]G[2] + G[1]G[1] + G[2]G[0] = 1*2 + 1*1 + 2*1 = 5

#Clarifying Questions:
#Do the values matter or just the structure? Just structure, how many can it form
#Is there an efficient way, or do I need to enumerate all trees? You only need the count. There is a neat DP or math formula!

#Approach: Dynamic Programming (Catalan Numbers)
#Let’s define G(n) = number of unique BSTs with n nodes.
#Key observation:
#For each possible root value i (from 1 to n):
#The left subtree has i-1 nodes (all numbers < i)
#The right subtree has n-i nodes (all numbers > i)
#The total number of trees with root i is: G(i-1) * G(n-i)
#Sum this over all i (from 1 to n):
"""
G(n) = G(0) * G(n-1) +
       G(1) * G(n-2) +
       G(2) * G(n-3) +
       ...
       G(n-1) * G(0)
Base case: G(0) = 1 (empty tree), G(1) = 1 (single node)
       """