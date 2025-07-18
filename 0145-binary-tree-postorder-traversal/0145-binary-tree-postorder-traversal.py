# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []                # If tree is empty, return []

        res = []                     # List to store postorder result
        stack = [root]               # Start with root node in the stack

        while stack:
            node = stack.pop()       # Pop node from stack
            res.append(node.val)     # Add node's value to result list
            # Push left first, so right is processed before left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]             # Reverse the result to get Left-Right-Root order

# Time Complexity: O(n)
#   - Each node is pushed and popped exactly once, for n nodes: O(n)
# Space Complexity: O(n)
#   - Result list O(n), stack O(h) in practice (worst-case O(n) for skewed tree)

# Dry Run
# Example: root = [1, None, 2, 3]
#         1
#          \
#           2
#          /
#         3
#
# stack = [1]
# pop 1 → res = [1], stack = [], push left(None), push right(2): stack = [2]
# pop 2 → res = [1,2], stack = [], push left(3), push right(None): stack = [3]
# pop 3 → res = [1,2,3], stack = []
# return res[::-1] = [3,2,1]

# Clarifying Questions:
# - Is the input a valid binary tree?
# - Is it given as TreeNode or list?
# - What should I return for an empty tree? (Return [])
# - Can I use a stack for iterative? (yes)
# - Should I solve recursively or iteratively? (either is fine unless interviewer restricts)

# Summary/One-liner to remember:
# - "Simulate reversed preorder (Root-Right-Left), then reverse output for postorder (Left-Right-Root)."
