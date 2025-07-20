# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]    #global var res

        #return the ax path sum without split
        def dfs(root):      #recursive dfs
            if not root:    #if node is null, add nothing
                return 0

            leftmax = dfs(root.left)    #get left max path
            rightmax = dfs(root.right)  #get right max path
            leftmax = max(leftmax, 0)   #they can be negative so update them
            rightmax = max(rightmax, 0)

            #compute max path sum WITH split
            res[0] = max(res[0], root.val + leftmax + rightmax)
            return root.val + max(leftmax, rightmax)    #return without splitting

        dfs(root)   #return the root, updates the global variable
        return res[0]


#time complexity: O(n)  Each node visited once.
#Space Complexity: O(h) Recursion stack (h = height of tree)

#Clarifying questions:
#Are node values negative? Yes, node values can be negative (as shown in the examples).
#Can the path start and end anywhere? Yes, the path can start and end at any node — does not have to pass through the root.
#Is a path a single node allowed? Yes, since a path can be of length 1.
#What if all node values are negative? The max path sum will just be the least negative single node value.

#Dry Run root = [-10,9,20,null,null,15,7]
# res = [-10], dfs(9) -> res = [9]
# dfs(20) _>  dfs(15) res = 15, dfs(7) res = 15
#dfs(20) = max(20, 42) res = 42
#dfs(-10) = max(-10, 9, 42) res = 42


"""
Explain the approach by drawing 
Approach
Key Insight:
The maximum path can pass through any node, and at each node, the max path may:
Go only left subtree
Go only right subtree
Go through current node (left + node + right)
Just the node itself (if everything else is negative!)
For every node, calculate:
The maximum gain it can contribute to its parent (one child only: left or right, not both, else it’s not a path).
But update the answer with left gain + node + right gain at every node (that’s a path passing through this node).
Strategy:
Do a post-order DFS.
At each node:
Recursively get max path sum from left/right.
If those are negative, treat them as 0 (ignore).
Compute local max (left + node + right) and update the global answer.
Return node + max(left, right) for recursion upward.
"""