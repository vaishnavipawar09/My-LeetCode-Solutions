# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Helper function to validate the BST property recursively.
        # left and right are the valid bounds for the current node.
        def valid(node, left, right):
            if not node:   # If the current node is None, it's valid (base case for empty subtree)
                return True
            # If the current node's value does NOT satisfy BST property, return False
            if not (node.val < right and node.val > left):
                return False
            # Check recursively:
            #   - The left subtree must have all values < node.val (update right bound)
            #   - The right subtree must have all values > node.val (update left bound)
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        
        # Start recursion with initial bounds (-infinity, +infinity)
        return valid(root, float("-inf"), float("inf"))

#Time Complexity: O(n)
#Space Complexity: O(n)