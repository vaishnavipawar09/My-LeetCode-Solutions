"""
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
        return root                 #Return the root (tree)

#Time Complexity: O(n)
#Space Complexity: O(n)
        


#Clarifying questions:
#Is the tree a standard binary tree or could it be a bst? binary tree
#can the tree be empty and have only one node? yes
#should i invert the tree in place or create a new tree and return the root? inplace is more efficient 
#are there any constraints on the node value? 0 to 100
#what should i return if the tree is empty? null or empty root? []

#Tree [1, 2, 3] _> [1, 3, 2]
# I notice for every node, we simply swap its left and right children. We can do this recursively (DFS), or iteratively using a queue (BFS). Both work since the tree isn't large.

class TreeNode:
    def __init__(self, val = 0, left = None, roiht = None):
        self.val = val
        self.left = left
        self.right = right 
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        