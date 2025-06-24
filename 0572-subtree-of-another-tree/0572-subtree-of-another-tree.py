# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If root is None, can't have any subtree except empty, so False
        if not root:
            return False
        # If subRoot is None, any tree contains an empty subtree, so True
        if not subRoot:
            return True
        
        # Check if the trees match at the current node, or check subtrees
        if self.isSameTree(root, subRoot):
            return True
        # Otherwise, recursively check left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    # Helper function: checks if two trees are identical
    def isSameTree(self, p, q):
        if not p and not q: #if both the tree are none, that means they are same so return True
            return True
        if not p or not q or p.val != q.val: #if even one is empty, no same tree, so False, or if val dont match
            return False
        #here we check if both are not empty, then check if their values match, also check the left and right subtree
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

#Time Complexity: O(m * n)
#Space Complexity: O(m + n), m is nodes on subtree, n nodes on root