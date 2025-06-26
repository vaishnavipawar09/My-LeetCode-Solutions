# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
Best Solution to solve is this by Neetcode
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

#Time Complexity: O(n^2) this is worst case
#Space Complexity: O(n)
"""

#Method 2 : DFS but Optimal
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIdx = inIdx = 0                  #start the two ptr at the start

        def dfs(limit):                     #create the helper function
            nonlocal preIdx, inIdx          #set to nonlocal

            if preIdx >= len(preorder):     #condition to cal the left subtree, if it goes over the len return None
                return None
            if inorder[inIdx] == limit:     #if the ind matches the limit, for right subtree
                inIdx += 1                  #increment the inorder index
                return None

            root = TreeNode(preorder[preIdx])   #set root at start, which will at the start of preorder
            preIdx += 1                         #move through the preorder list
            root.left = dfs(root.val)           #recursion to create the left subtree
            root.right = dfs(limit)             #recursion to create the right subtree
            return root                         #return the root
        return dfs(float('inf'))                #return and close the function
        

#Time Complexity: O(n)
#Space Complexity: O(n)

