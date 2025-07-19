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


        while q:                #while q is not empty, iterates through the whole tree           O(n)
            qlen = len(q)       #cal the length of the queue
            rightside = None    #initialize rightside to None

            for i in range(qlen):   #itearate through the whole queue                           O(n)
                node = q.popleft()  #as it is FIFO, we always pop from left, pop the node out and add its children 
                if node:            #if the node is not empty and has children append it to the queue
                    rightside =node #set the rightside o the node
                    q.append(node.left) #add the left and right child nodes to the queue
                    q.append(node.right)
            if rightside:           #if rightside not empty
                res.append(rightside.val)   #add only the right side node values to the result list
        return res                  #return the lisyt containing only rightside
        
# -- Dry Run Example (with comments):
# root = [1,2,3,null,5,null,4]
# Tree:
#         1
#       /   \
#      2     3
#       \     \
#        5     4
#
# Initial: q = [1], res = []
# Level 1: qlen = 1, pop 1, q=[2,3], rightmost (1), res=[1]
# Level 2: qlen = 2, pop 2 (q=[3]), add 5; pop 3 (q=[5,4]), add 4; rightmost (3), res=[1,3]
# Level 3: qlen = 2, pop 5 (q=[4]), pop 4 (q=[]), rightmost (4), res=[1,3,4]
# End: q is empty. Return res = [1,3,4]

# Time Complexity: O(n)
# - Each node is processed once in the BFS traversal.
# - The inner for loop runs exactly n times (once per node).
# Space Complexity: O(n)
# - The queue at most holds all nodes at one level (up to n in worst case).
# - The result list holds at most n values.



#Clarifying questions:

#Is the input always a valid binary tree?
#Is the input a TreeNode structure?
#What should I return if the tree is empty? (Return [])
#Are negative or duplicate node values possible? (Yes)
#If two nodes are at the same level and visible from the right, do I only include the rightmost? (Yes)
#Can I use extra space for queues (BFS)? (Yes, as usual BFS solution is allowed)


#Approach Statement: “Do a level order BFS and record the last node at each level—those are the rightmost visible from the side.”
#[1,2,3,null,5,null,4] → [1,3,4]
#[1,2,3,4,null,null,null,5] → [1,3,4,5]

#Why BFS? BFS naturally visits nodes level by level, so it’s very easy to identify which node is the last one at every level.
#We use BFS because it lets us process the tree one level at a time, and the queue helps us remember the order in which nodes should be visited. That makes it easy to record the last node at each level—the “right side view.”