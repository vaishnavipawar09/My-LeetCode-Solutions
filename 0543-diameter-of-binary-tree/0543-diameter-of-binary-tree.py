# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0  # This variable will store the maximum diameter found

        def dfs(root):
            nonlocal res  # Allows inner function to update 'res' from enclosing scope

            if not root:
                return 0  # Base case: empty subtree has depth 0

            # Recursively find the depth of left and right subtrees
            left = dfs(root.left)
            right = dfs(root.right)

            # Update the result: diameter at this node is left_depth + right_depth
            res = max(res, left + right)

            # Return the depth of the current subtree for parent calls
            return 1 + max(left, right)

        dfs(root)      # Start DFS traversal from root
        return res     # The result holds the largest diameter found


    #Time Complexity: O(n)  Each node is visited exactly once.
    #Space Complexity: O(n)  h = height of the tree (due to recursion stack; O(n) in worst case for skewed tree).

'''
#Method 2 : Iterative DFS using Stack and hashmap
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]                # Initialize stack for iterative traversal
        mp = {None: (0, 0)}           # Hashmap: maps node to (height, diameter); None's height/diameter = 0

        while stack:
            node = stack[-1]          # Peek at the top node
            
            # If left child not processed, push it to stack
            if node.left and node.left not in mp: #if nodeleft empty and not present in hashmap
                stack.append(node.left)
            # If right child not processed, push it to stack
            elif node.right and node.right not in mp: #if noderight empty and not present in hashmap
                stack.append(node.right)
            else:
                node = stack.pop()    # Both children processed; now process this node
                leftHeight, leftDiameter = mp[node.left]
                rightHeight, rightDiameter = mp[node.right]
                # Height: 1 + max of left/right child heights
                # Diameter at this node: max of (left+right heights), left diameter, right diameter
                mp[node] = (1 + max(leftHeight, rightHeight), 
                            max(leftHeight + rightHeight, leftDiameter, rightDiameter))
        
        return mp[root][1]            # Return diameter stored for root


    #Time Complexity: O(n) 
    #Space Complexity: O(n)  

    '''


"""
Step 1: Clarifying Questions
Is the input always a valid binary tree (no cycles, connected)? Yes, assume the input is a valid binary tree.
How is the input provided? As a TreeNode (LeetCode standard), not as an array.
What should I return if the tree only has one node? Return 0 (since the diameter is the number of edges in the longest path, a single node has 0 edges).
Can node values be negative or duplicated? Node values can be any integer (irrelevant for this problem; only structure matters).
Are all nodes unique? Yes, but again, node values don't affect the diameter.

Step 2: Test Cases / Edge Cases
root = [1] → Output: 0 (Single node, diameter = 0)
root = [1,2] → Output: 1 (Path: [2,1])
root = [1,2,3,4,5]

        1
       / \
      2   3
     / \
    4   5
Longest path: [4,2,1,3] (edges = 3)

Step 3: Approach / Pseudocode
The diameter is the longest path between any two nodes (measured by edges).
For each node, the longest path passing through it = (max depth of left subtree) + (max depth of right subtree).
Use DFS (post-order traversal):
For each node:
Recursively get the depth of left and right subtrees.
Update the diameter if left_depth + right_depth is greater than current max.
Return 1 + max(left_depth, right_depth) for recursion.

Step 6: Dry Run (for example 1: root = [1,2,3,4,5])
At node 4: left=0, right=0 → diameter = max(0, 0+0) = 0 → returns 1
At node 5: left=0, right=0 → diameter = max(0, 0+0) = 0 → returns 1
At node 2: left=1, right=1 → diameter = max(0, 1+1) = 2 → returns 2
At node 3: left=0, right=0 → diameter = max(2, 0+0) = 2 → returns 1
At node 1: left=2, right=1 → diameter = max(2, 2+1) = 3 → returns 3
Return value: 3
"""