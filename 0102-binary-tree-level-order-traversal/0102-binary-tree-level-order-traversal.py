# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:        #handle base case if root is none
            return []
        
        res = []                #create one to store result
        q = collections.deque() #initailize the queue
        q.append(root)          #first value to be added to the queue is the root value

        while q:                #while q is not empty, iterates through the whole tree
            qlen = len(q)       #cal the length of the queue
            level = []          #temp var to calculate the level 
            for i in range(qlen):   #itearate through the whole queue
                node = q.popleft()  #as it is FIFO, we always pop from left, pop the node out and add its children 
                if node:            #if the node is not empty and has children append it to the queue
                    level.append(node.val)  #Update the level if adding the children
                    q.append(node.left)     #add the left and right child nodes to the queue
                    q.append(node.right)
            if level:               #if level is not empty, update the res with the level
                res.append(level)
            
        return res              #return the max level

#Time Complexity: O(n)
#Space Complexity: O(n), cause we are a=using queue


        