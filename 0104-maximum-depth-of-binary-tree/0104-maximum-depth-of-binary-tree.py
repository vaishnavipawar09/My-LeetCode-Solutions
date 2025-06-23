# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:                #Handles all the base case, if the root is empty, there is no depth 
            return 0
        else:
            leftdepth = self.maxDepth(root.left)            #Using recursion we found the depth of left child
            rightdepth = self.maxDepth(root.right)          #Using recursion we found the depth of the right child
            return max(leftdepth, rightdepth) + 1         #max of left and right child depth, 1 is the depth of the root

        
    #Time Complexity: O(n)
    #Space Complexity: O(n)
        