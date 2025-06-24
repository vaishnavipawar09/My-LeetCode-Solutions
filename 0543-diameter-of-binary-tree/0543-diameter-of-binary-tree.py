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


    #Time Complexity: O(n) 
    #Space Complexity: O(n)  

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