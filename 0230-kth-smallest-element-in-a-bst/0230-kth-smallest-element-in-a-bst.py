# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []              #intialize a stack 
        curr = root             #set curr to root
        n= 0                    #intialized a counter
        while stack or curr:    #while the stack and curr nodes are not empty
            while curr:         #while curr is not empty 
                stack.append(curr)  #add the curr val to the satck
                curr = curr.left    #shift frm the root node to the left subtree
            curr = stack.pop()      #pop from the stack 
            n += 1                  #update the counter
            if n == k:              #if cnt is equal to the k value
                return curr.val     #we return the node, value, found it 
            curr = curr.right       #then we can start going to the right subtree


#Time Complexity: O(n)
#Space Complexity: O(n)
        