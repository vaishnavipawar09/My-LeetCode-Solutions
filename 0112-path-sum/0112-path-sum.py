# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        if not root.left and not root.right:    ## If this is a leaf node, check if the value matches the remaining targetSum
            return root.val == targetSum
        return (self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val))
"""
#Dry Run
# root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
        5
       / \
      4   8
     /   / \
   11  13  4
  /  \      \
 7    2      1

 TargetSum: 22

Start at root (5), targetSum=22. 22-5=17.
Go left to 4, targetSum=17. 17-4=13.
Go left to 11, targetSum=13. 13-11=2.
Go left to 7, targetSum=2. 2-7=-5 (Not a leaf that sums to target)
Backtrack to 11, go right to 2. 2-2=0.
2 is a leaf and targetSum matches!
Return True.

"""

#“Subtract the node’s value from the target as you traverse; if you reach a leaf and hit zero, you’ve found the path.”

#Time & Space Complexity
#Time Complexity: O(N)
#Each node is visited once, where N = number of nodes.

#Space Complexity: O(H)
#H = height of tree (for recursion stack). Worst-case O(N) for a skewed tree, O(log N) for a balanced tree

#Claifying Questions:
#Is the input always a valid binary tree? (Yes)
#Are negative numbers possible in node values or targetSum? (Yes, as per constraints)
#Should we return False if the tree is empty? (Yes)
#Do we care about all paths or just root-to-leaf? (Only root-to-leaf)
#Are duplicate values allowed in the tree? (Yes)
#Can there be multiple valid paths from the root?


#Edge: root = [], targetSum = 0 ⇒ Output: False
#root = [1,2,3], targetSum = 3 ⇒ Output: True (Path: 1→2)
#oot = [1,2,3], targetSum = 5 ⇒ Output: False
#root = [1,-2,-3,1,3,-2,None,-1], targetSum = -1 ⇒ Output: True
#Multiple valid paths: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22 ⇒ Output: True

#Approach
#This is a classic DFS (Depth-First Search) recursion problem:
#Traverse from the root to each leaf, subtracting the current node’s value from targetSum.
#If you reach a leaf and the remaining sum is 0, return True.
#If you never find such a path, return False.

