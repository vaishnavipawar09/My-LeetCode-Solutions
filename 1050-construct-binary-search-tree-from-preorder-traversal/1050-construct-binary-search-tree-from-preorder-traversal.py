# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        index = 0
        def buildBST(bound):            #Helper function buildBST(bound) builds a subtree whose node values must be < bound.
            nonlocal index              #nonlocal index lets us modify the index defined outside the helper.

            #If we've used up all nodes, return None.
            #If the next node's value is too large (doesn’t fit this subtree’s bound), return None.
            if index == len(preorder) or preorder[index] > bound:       
                return None
            
            val = preorder[index]       #We build a TreeNode with the next value in preorder.
            node = TreeNode(val)
            index +=1                   #Move index forward, as we've now "used" this value.
            node.left = buildBST(val)   ## left subtree: values < val
            node.right = buildBST(bound)    # right subtree: values < bound but > val
            return node
        return buildBST(float('inf'))

# Dry Run for [8,5,1,7,10,12]:
# index=0, bound=inf, root=8
#   index=1, bound=8, root=5
#       index=2, bound=5, root=1 (left), index=3, 7>1 so right
#           index=3, bound=5, 7>5 so return None for right of 1
#       index=3, 7<5 is False, so right child of 5 is 7
#   index=4, 10>8 is False, right child of 8 is 10
#       index=5, 12<10 is False, right child of 10 is 12

#Time: O(n), each node is processed exactly once.
#Space: O(n) for the recursion stack in the worst case (skewed tree).


#Clarifying Questions:
#Are all values in preorder unique? (Yes, per constraints.)
#Is the input guaranteed to represent a valid BST preorder? (Yes.)
#Should I return the root of the reconstructed BST? (Yes.)
#How large can the input be? (Up to 100 nodes.)
#Can I assume standard TreeNode class? (Yes, per LeetCode conventions.)

# preorder = [8,5,1,7,10,12] -> [8, 5, 10, 1, 7, null, 12]

#Preorder for BST means the first number is always the root., 
#All numbers after the root that are less go to the left, and all numbers greater go to the right (because it's a BST).
#The subarrays for left and right are determined by the BST property, not just splitting by size or index.

#Approach
#Use an index to track our position in the preorder array.
#Use recursion with upper/lower bounds:
#For each subtree, only allow numbers within its valid range.
#At each call:
#Take the next value as the node.
#Recurse to build left subtree (values less than current).
#Recurse to build right subtree (values greater than current).

"""
Use the BST property: For each subtree, every value must be less than an upper bound.
Use the preorder property: The next element is always the root of the next subtree.
Use an index (not slicing arrays!) to track position in preorder.
Use recursion with bounds to enforce BST rules.

Key Interview Points
Recursive construction using bounds is optimal and fast.
No slicing or copying of arrays—just index and bounds.
Preorder traversal directly constructs the tree.
"""