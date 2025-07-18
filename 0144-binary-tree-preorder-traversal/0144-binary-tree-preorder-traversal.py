# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []                    # Result list for node values
        stack = []                  # Stack for nodes (LIFO)
        if root:
            stack.append(root)      # Start with root in stack

        while stack:                # While there are nodes to process
            node = stack.pop()      # Pop from stack
            res.append(node.val)    # Visit: add value to result (Root first)
            if node.right:
                stack.append(node.right)   # Push right first (so left comes out first)
            if node.left:
                stack.append(node.left)    # Then push left child

        return res

# Time Complexity: O(n)
#   Each node is visited once, each node pushed/popped from stack at most once.
# Space Complexity: O(n)
#   Result list O(n), Stack O(h) (h=tree height), worst-case O(n) for skewed tree.

# Dry Run
# root = [1, null, 2, 3]
# Stack: [1], res: []
# Pop 1 → res=[1], push right (2): stack=[2]
# Pop 2 → res=[1,2], push right (3): stack=[3]
# Pop 3 → res=[1,2,3], stack=[]
# Output: [1,2,3]

# Clarifying Questions:
# - Is the input a valid binary tree?
# - Is it a TreeNode class or array?
# - What to return for empty tree? (Return [])
# - Can I solve recursively or iteratively?
# - Any space restrictions on the iterative version?
