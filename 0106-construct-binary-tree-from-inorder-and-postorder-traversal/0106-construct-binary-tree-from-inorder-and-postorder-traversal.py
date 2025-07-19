# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        postIdx = len(postorder) - 1   # Start at the end of postorder
        inIdx = len(inorder) - 1       # Start at the end of inorder

        def dfs(limit):
            nonlocal postIdx, inIdx
            if postIdx < 0:
                return None
            if inorder[inIdx] == limit:
                inIdx -= 1
                return None
            
            root = TreeNode(postorder[postIdx]) #last indx of postorder will always be the root
            postIdx -= 1                        #decrement the index as we are reversing
            # Build right first, then left! (since postorder is L-R-root, and we're going backwards)
            root.right = dfs(root.val)
            root.left = dfs(limit)
            return root

        return dfs(float('inf'))

#Time Complexity: O(n)
#Space Complexity : O(n)

    """1. Clarifying Questions

Is every value in the tree unique? (Yes, per constraints.)

Are both traversals of the same tree and cover all nodes? (Yes.)

Can values be negative or zero? (Yes.)

How large can the tree be? (Up to 3000 nodes.)
"""