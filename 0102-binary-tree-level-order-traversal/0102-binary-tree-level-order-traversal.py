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

#Time Complexity: O(n), where n = total nodes. Every node is enqueued and dequeued once.
#Space Complexity: O(n) for the result + O(w) for the queue, where w is the max width of the tree (could be O(n) in worst case, e.g., a full binary tree bottom level).

#Dry Run
#root = [3,9,20,null,null,15,7]
#- Initial queue: [3]
# Level 1: Pop 3 → level=[3], append 9, 20 → queue=[9,20]
# Level 2: Pop 9, 20 → level=[9,20], append 15, 7 → queue=[15,7]
# Level 3: Pop 15, 7 → level=[15,7], queue=[]
# Result: [[3], [9,20], [15,7]]

#Clarifying question:
#Is the input given as a TreeNode class or a list/array?
#What should I return if the tree is empty (root is None)? []
#Should each level’s values be grouped in a separate list, from top to bottom?
#Should traversal be strictly left-to-right within each level?
#Is there any restriction on auxiliary data structures, or can I use a queue?

# ip: [] -> []
#root =  [1] -> [[1]]
#[3, 9, 20, null, null,15, 7 ] -> [[3], [9, 20], [15, 7]]
