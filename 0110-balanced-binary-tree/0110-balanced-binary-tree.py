# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:                        # If there’s no node here, it’s balanced and height is 0
                return [True, 0]

            left = dfs(root.left)               # Recursively check left and right subtrees
            right = dfs(root.right)

            # A node is balanced if:
            # 1. Both its left and right subtrees are balanced
            # 2. The difference in height between left and right is at most 1
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1           
            return [balanced, 1 + max(left[1], right[1])]     # Return [Is this subtree balanced?, What’s its height]
       
        return dfs(root)[0]     # The final answer is whether the whole tree is balanced (just the bool part!)
