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

#Time Complexity: O(m * n), m = number of nodes in root, n = number of nodes in subRoot.
#In worst case, for every node in root, you might compare the whole subRoot (nested recursion).

#Space Complexity: O(m + n), m is nodes on subtree, n nodes on root, O(h), where h is the height of the root tree (for recursion stack).


"""
1. Clarifying Questions
Is the input guaranteed to be valid binary trees? Yes.
Can subRoot be the whole root tree? Yes, the entire tree can be a subtree of itself.
Do node values have to match exactly, including structure? Yes, both structure and values must match.
Can the trees have duplicate values? Yes, values can be duplicated.
What should I return if subRoot is larger than root? Always False (based on constraints, won't happen).
Should I handle empty trees? Input always has at least 1 node (per constraints).

2. Test Cases / Edge Cases
root = [1], subRoot = [1] → True
root = [1], subRoot = [2] → False
root = [3,4,5,1,2], subRoot = [4,1,2] → True
root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2] → False

3. Approach
High-level: For every node in root, check if the subtree starting at that node is identical to subRoot.
Use a helper function to compare two trees for equality.
Steps:
For each node in root:
If isSame(node, subRoot) is True, return True.
Otherwise, recursively check left and right subtrees.
If you reach the end without finding a match, return False.

6. Dry Run (with example 1)
root = [3,4,5,1,2], subRoot = [4,1,2]
Start at 3: 3 ≠ 4, not a match.
Go to left child 4: isSame(4, 4) → yes. Then, check isSame(1, 1) → yes, isSame(2, 2) → yes. All structure matches.
Return True.
"""