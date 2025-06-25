# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:        #handle base case if root is none
            return []
        
        res = []                #create one to store result
        q = collections.deque() #initailize the queue
        q.append(root)          #first value to be added to the queue is the root value


        while q:                #while q is not empty, iterates through the whole tree
            qlen = len(q)       #cal the length of the queue
            rightside = None    #initialize rightside to None

            for i in range(qlen):   #itearate through the whole queue
                node = q.popleft()  #as it is FIFO, we always pop from left, pop the node out and add its children 
                if node:            #if the node is not empty and has children append it to the queue
                    rightside =node #set the rightside o the node
                    q.append(node.left) #add the left and right child nodes to the queue
                    q.append(node.right)
            if rightside:           #if rightside not empty
                res.append(rightside.val)   #add only the right side node values to the result list
        return res                  #return the lisyt containing only rightside
        
#Time Complexity: O(n)
#Space Complexity: O(n)