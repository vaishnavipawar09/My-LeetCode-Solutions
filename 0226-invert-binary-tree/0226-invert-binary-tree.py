
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:        #This handles all the edge cases, even th left and right node cases 
            return root
        #Using a temp var to swap the left and the right nodes of the tree
        temp = root.left
        root.left = root.right
        root.right = temp
        
        self.invertTree(root.left) #Use recusrion to swap the left nodes child, here the base caseis handled by above
        self.invertTree(root.right) #Use recusrion to swap the right nodes child, here the base caseis handled by above
        return root                 #Return the root (tree)

#Time Complexity: O(n)
#The function starts at the root., For every node, it swaps its left and right children (O(1))., a constant amount of work
#Then it makes recursive calls on the left and right children., This process continues until all nodes are visited.
#No node is visited more than once, So if there are n nodes, the function runs in O(n) time.

#Space Complexity: O(n) = O(h), h = height of the tree.
#In the worst case (a skewed tree, like a linked list), h = n → so O(n).
#In the best/average case (a balanced tree), h = log n → O(log n).
#his is due to the recursion stack,At any moment, the maximum number of function calls in the stack is equal to the height of the tree.

#Dry Run
#[4, 2, 7, 1, 3, 6, 9]
# 1. root = 4, root.left = 7, root.right = 2  [4, 7, 2, 1, 3, 6, 8]
# 2. root = 4, root.left invertTree(7), root.left= 9 root.right = 6
# 3. invertTree(9) None, no effect, rturn node 9
# 4. invertTree(6) None, no effect, return node 6
# 5. invertTree(2), root.left = 3, root.right = 1
# 6. invertTree(3), none, no effect , rturn 3
# 7. invertTree(1), none, no effect, return 1
# 8. root = [4, 7, 2, 9, 6, , 3, 1]


# [1,2, 3]->[1, 3, 2]
# root = 1, temp =2, root.left = 3, root.right = 2
# root.left = 3 
# root.right = 2
# root = [1, 3, 2]

"""   
#Self practice:
#Clarifying questions:
#Is the tree a standard binary tree or could it be a bst? binary tree
#can the tree be empty and have only one node? yes
#should i invert the tree in place or create a new tree and return the root? inplace is more efficient 
#are there any constraints on the node value? 0 to 100
#what should i return if the tree is empty? null or empty root? []

#Tree [1, 2, 3] _> [1, 3, 2]
# I notice for every node, we simply swap its left and right children. We can do this recursively (DFS), or iteratively using a queue (BFS). Both work since the tree isn't large.

class TreeNode:
    def __init__(self, val = 0, left = None, roiht = None):
        self.val = val
        self.left = left
        self.right = right 
#DFS
class Solution:
    def invertTree(self, root:Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        root.left , root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

#BFS
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

           
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left , node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
"""