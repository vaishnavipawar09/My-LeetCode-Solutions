# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None: #if both the tree are none, that means they are same so return True
            return True
        if p is None or q is None:      #if even one is empty, no same tree, so return False
            return False

        #here we check if both are not empty, then check if their values match, also check the left and right subtree
        return (p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        # All conditions must be True for trees to be identical.

#Time Complexity: O(n)
#Space Complexity: O(n)

'''
#Neetcode solution: Same thing as above 
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:  #here just checks if p and q are not empty and the values match
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

'''