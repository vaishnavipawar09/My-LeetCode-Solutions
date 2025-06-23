# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:        #This handles all the edge cases, even th left and right node cases 
            return root
        #Using a temp var to swap the left and the right nodes of the tree
        temp = root.left
        root.left = root.right
        root.right = temp
        
        self.invertTree(root.left) #Use recusrion to swap the left nodes child, here the base caseis handled by above
        self.invertTree(root.right) #Use recusrion to swap the right nodes child, here the base caseis handled by above
        return root

#Time Complexity: O(n)
#Space Complexity: O(n)
        