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


#time complexity: O(n)
#Space Complexity: O(n)