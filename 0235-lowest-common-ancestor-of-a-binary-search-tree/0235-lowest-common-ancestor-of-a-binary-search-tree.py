# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root

        curr = root                                     #Set you rcurr val to the root val
        while curr:                                     #loop thrugh the whole tree until null
            if p.val < curr.val and q.val < curr.val: #if p & q values < the current val, move to left subrtree
                curr = curr.left                        #shift your curr to the left side
            elif p.val > curr.val and q.val > curr.val: #if p & q are > te curr value, move the search to right subtree
                curr = curr.right                       #shift your curr to the right subtree
            else:                                       #found the split pt or match that is lca
                return curr                          #found the lca at the curr post, pval is on left and qval is right
        
        #Time Complexity: O(h), height of the tree
        #Space Complexity: O(1)