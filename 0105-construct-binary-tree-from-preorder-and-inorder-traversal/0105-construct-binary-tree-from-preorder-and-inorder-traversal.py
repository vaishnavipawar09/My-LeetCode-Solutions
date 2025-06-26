# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

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
        preIdx = inIdx = 0

        def dfs(limit):
            nonlocal preIdx, inIdx

            if preIdx >= len(preorder):
                return None
            if inorder[inIdx] == limit:
                inIdx += 1
                return None

            root = TreeNode(preorder[preIdx])
            preIdx += 1
            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root
        return dfs(float('inf'))
        

#Time Complexity: O(n)
#Space Complexity: O(n)


"""