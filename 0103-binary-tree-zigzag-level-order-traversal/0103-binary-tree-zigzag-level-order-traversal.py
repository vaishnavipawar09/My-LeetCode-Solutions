# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
                level.append(node.val)
                if node.left:       #if not not empty and has childrens, add left and right child to the queue
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if len(res) % 2:                    #Checks if the given level is an even or odd
                level = list(reversed(level))   #if odd it reverses
            res.append(level)                   #add the level to the result

        return res              #return the max level

