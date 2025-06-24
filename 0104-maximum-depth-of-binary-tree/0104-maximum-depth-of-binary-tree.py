# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
#Method 1 : Using Recursion
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:                #Handles all the base case, if the root is empty, there is no depth 
            return 0
        else:
            leftdepth = self.maxDepth(root.left)            #Using recursion we found the depth of left child
            rightdepth = self.maxDepth(root.right)          #Using recursion we found the depth of the right child
            return max(leftdepth, rightdepth) + 1         #max of left and right child depth, 1 is the depth of the root

    #Time Complexity: O(n)
    #Space Complexity: O(n)


#Method 2 : Using Iterative DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]     #Add pair of values, the root and the depth
        res = 0         #set to 0, cause if we have a null node, th if wont execute

        while stack:
            node, depth = stack.pop()   #we are popping 2 values, the node and the depth

            if node:            #if node not null
                res = max(res, depth)       #res max of itself
                stack.append([node.left, depth + 1])    #add the children of left and the depth
                stack.append([node.right, depth + 1])   #add the children of right with depth 
        return res                  #return the res

#Time Complexity: O(n)
#Space Complexity: O(n)
'''
#Method 3 : Using BFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:                #Handles all the base case, if the root is empty, there is no depth 
            return 0

        level = 0                  #our curr level is zero
        q = deque([root])
        while q:                    #until the queue is empty
            for i in range(len(q)): #Traverse the entire level in the q
                node = q.popleft()  #Pop from the left of the node and add its children
                if node.left:            #Add left child, if node.left is not empty
                    q.append(node.left)
                if node.right:           #Add right child, if node.left is not empty
                    q.append(node.right)
            level += 1              #increase the level
        return level                #if queue is empty return the total no. of level
#Time Complexity: O(n)
#Space Complexity: O(n)
