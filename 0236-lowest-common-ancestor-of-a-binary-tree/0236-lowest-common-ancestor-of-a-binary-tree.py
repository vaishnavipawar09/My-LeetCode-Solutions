# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:      # If root is None, or we've found p or q, return root
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left or right 


# root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# root = 3,is root 5 or 1 nope
#recurse left(5), right (1)
# mode 5 p==5 yes  return 5 to call stack
# node == 1 equal to p and q no
# traverse on the node 1s left, and right returns none
# if left and right , lca = 5

#Dry Rune 2
# Start at root (3). Not p or q.
# Go left to 5. That’s p!
# Search 5’s left (6) — not q, returns None.
# Search 5’s right (2):
# 2’s left (7) — not q, returns None.
# 2’s right (4) — that’s q! Returns 4.
# So, left of 5: None, right of 5: 4.
# Since 5 is p and found q below, LCA is 5!

#Clarifying questions:
#Is it guaranteed to be a Binary tree
#will p and q exists in the tree
# are all the node values unique
# if a tree is empty should i return a 0 or empty tree
# can p and q be the root ? 
# will p be equal to q no p ! = q
#Should i return the node itself or just the value? 
#Can p and q be direct parent/ child? yes
#what if p is the ancestor of q or vise versa? 