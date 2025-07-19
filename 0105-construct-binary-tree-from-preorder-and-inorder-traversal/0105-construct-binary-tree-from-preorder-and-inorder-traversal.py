# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Best Solution to solve is this by Neetcode

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:         #Base Case if not preorder or inorder return none
            return None
        
        root = TreeNode(preorder[0])            #First value in th preorder is always the root (RootLR)
        mid = inorder.index(preorder[0])        #mid calculates the index where the root is in the inorder (LRootR)

        #Left subtree in preorder is mostly directly after root, and in inorder it is first and then root
        root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid]) 
        #Right subtree in preorder is mostly directly after the left, and in inorder it is last after the root
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root                             #Return the tree nodes

#Dry Run: preorder [3, 9, 20, 15, 7]  inorder [9, 3, 15, 20, 7]
# root= 3, mid = 1 inorder[1] leftsubtree preorder[1:2] inorder[0:1] = 9
# root = 9 null 
# right subtree preorder[2:4] = [20, 15, 7] inorder[2:4]= [15, 20, 7]
# root = 20 found inorder[3] mid = 3,  left preorder[3:4] = 15 inorder[2:3] = 15
#right preorder[4:4] = 7 inorder[4:4] = 7

#Time Complexity: O(n^2) this is worst case
#Space Complexity: O(n)

#Clarifying Questions:
#Are values unique in both arrays? Yes, by constraint.
#Are preorder and inorder both for the same tree? Yes.
#Will the arrays always be non-empty and of equal length? Yes.
#Is TreeNode definition provided? Assume yes, as per LeetCode.
#Can we assume valid input (i.e., arrays correspond to a valid binary tree)?Yes.

#preorder = [1], inorder = [1] → single node.
#preorder = [3,9,20,15,7], inorder = [9,3,15,20,7] → standard exampl

#3. Approach: Key Insight: Preorder: root, left, right. Inorder: left, root, right. The first value in preorder is always the root.
#In inorder, everything to the left of the root is in the left subtree, everything to the right is in the right subtree.
#Algorithm: Find the root in inorder. Recursively build left and right subtrees using slices of preorder/inorder.
#Optimization: Use a hashmap to store inorder value → index for O(1) lookup.

#“Preorder gives root; inorder slices left/right. Recursively build by finding root’s index in inorder.”
"""



#Method 2 : DFS but Optimal
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIdx = inIdx = 0                  #start the two ptr at the start

        def dfs(limit):                     #create the helper function
            nonlocal preIdx, inIdx          #set to nonlocal  lets us update the indexes across recursive calls.

            if preIdx >= len(preorder):     #condition to cal the left subtree, if it goes over the len return None
                return None
            if inorder[inIdx] == limit:     #if the ind matches the limit, for right subtree
                inIdx += 1                  #increment the inorder index
                return None

            root = TreeNode(preorder[preIdx])   #set root at start, which will at the start of preorder
            preIdx += 1                         #move through the preorder list
            root.left = dfs(root.val)           #recursion to create the left subtree Build everything before this root in inorder traversal (limit is root's value).
            root.right = dfs(limit)             #recursion to create the right subtree  Build everything up to the outer limit (i.e., whatever our parent’s limit was).
            return root                         #return the root
        return dfs(float('inf'))                #return and close the function 
                                                #Start building the entire tree, and use an impossible value (inf) as the "outermost" limit so we never stop early.


        

#Time Complexity: O(n)
#Space Complexity: O(n)

Let’s do a small dry run for preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]:
First call: dfs(float('inf'))
preIdx = 0, so root = TreeNode(3)
Build root.left = dfs(3)
preIdx = 1, so root = TreeNode(9)
Build root.left = dfs(9) (but inorder[inIdx] == 9, stop!)
Build root.right = dfs(3) (but inorder[inIdx] == 3, stop!)
So 9 has no children.
Build root.right = dfs(float('inf'))
Next root is 20, and so on…

Why Is This Optimal?
No slicing or copying arrays—just index updates, which is O(1).
Each node is visited exactly once (O(n) time and space).

How to Remember
“Rebuild the tree recursively, using preorder to pick the root, and use a 'limit' in inorder to know when a subtree ends. Move pointers instead of slicing arrays.”

"""