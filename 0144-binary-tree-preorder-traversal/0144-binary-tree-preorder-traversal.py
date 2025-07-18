# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        res = []                    #create a list for result
        stack =[]                   #create a stack 
        curr = root                 #assign root to the curr
        while curr or stack:
            while curr: 
                res.append(curr.val)
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            curr = curr.right
        return res

        