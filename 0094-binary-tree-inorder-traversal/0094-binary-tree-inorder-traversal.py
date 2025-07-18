# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []                    #create a list for result
        stack =[]                   #create a stack 
        curr = root                 #assign root to the curr

        while curr or stack:        #while curr and stack are not empty
            while curr:
                stack.append(curr)  #append the curr node to the stack and traverse to the left subtree
                curr = curr.left
            curr = stack.pop()      #once you encounter an empty or null, pop from the stack and append to the result 
            res.append(curr.val)
            curr = curr.right       #after the whole iteration move to the right subtree/node
        return res                  #return the result 

#Time Complexity : O(n)     
#Space Complexity : O(n) 

#Dry Run
# [1, null, 2, 3]
# res = stack = [], curr = 1, stack =[1] curr = null, pop res = [1], stack =[]
# curr = 2, stack =[2], curr = 3, , stack = [2, 3 ] 
# curr = 3  left no pop 3 stack = [2], res = [1, 3]
# stack [] res = [1, 3, 2]

#Clarifying Qi=uestions:
#Can I assume the input is a valid binary tree?
#Is the input given as a TreeNode class or as a list/array according to LeetCode
# if the tree is empty or null what should i return?  []
# Can i solve recursively or do you want be to solve iteratively?
#For the iterative solution, can I use a stack, or is there a restriction on extra space?

# eoot = []
# root =[1] -> [1]
# [1, null, 2, 3] -> [1, 3, 2]
