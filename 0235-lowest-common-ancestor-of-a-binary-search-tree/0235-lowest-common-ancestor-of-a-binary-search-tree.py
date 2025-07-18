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
        
#Time Complexity: O(h), where h is the height of the BST (O(log n) for balanced, O(n) for skewed tree).
#Space Complexity: O(1) for the iterative approach (no recursion stack).

#Dry Run:
#[6, 2, 8, 0, 4, 7, 9, null, null, 3, 5] p = 2, q = 8 LCA = 6
# curr = 6, 2<6 yes and 8< 6 no return curr = 6

#[6, 2, 8, 0, 4, 7, 9, null, null, 3, 5] p = 2, q = 4 LCA = ?
# curr = 6, 2< 6 yes, 4< yes curr.left = 2
# curr = 2, 2< 6 no, return curr, 2

#Clarifying Questions:
# will p and q guaranteed to exist in the BST ? yes
# Are all node values unique 
#Can p and q be root ? 
#is the tree guaranteed to be a BST ? 
# will p be equal to q
#Should i return the node itself or just the value? 
#Can p and q be direct parent/ child? yes
#what if p is the ancestor of q or vise versa? 

# [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5] p = 2, q = 8 LCA = 6
# p = 2, q = 4 LCA = 2

#Approach (Think out loud):
#Because this is a BST, all left descendants are < root and all right are >.
#So, if both p and q are < root, LCA is in the left subtree.
#If both > root, it’s in the right subtree.
#Otherwise, root is the split point, and hence the LCA.


class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left =  left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: Optional[TreeNode], q : [TreeNode]):
        if root is None:
            return root

        curr = root
        while root:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val> curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr


