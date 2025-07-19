# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:        #handle base case if root is none  O(1)
            return []
        
        res = []                #create one to store result     O(1)
        q = collections.deque() #initailize the queue
        q.append(root)          #first value to be added to the queue is the root value

        while q:                #while q is not empty, iterates through the whole tree
            qlen = len(q)       #cal the length of the queue
            level = []          #temp var to calculate the level 
            for i in range(qlen):   #itearate through whole queue In total, this inner loop runs O(n) times across all levels
                node = q.popleft()  #as it is FIFO, we always pop from left, pop node out and add its children O(1) per pop
                level.append(node.val)
                if node.left:       #if not not empty and has childrens, add left and right child to the queue
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if len(res) % 2:                    #Checks if the given level is an even or odd
                # O(k) for each level, where k = width of that level; across all levels, still O(n)
                level = list(reversed(level))   #if odd it reverses 
            res.append(level)                   #add the level to the result

        return res              #return the max level

#Time Complexity:


#Clarifying questions:
#Is the input always a valid binary tree (no cycles)?
#Is the input a TreeNode structure, not a list/array?
#What should I return if the tree is empty?
#Can node values be negative or duplicated?
#Is “zigzag” strictly alternating left-to-right and right-to-left at each level?


# root = [3,9,20,null,null,15,7] -> Output: [[3],[20,9],[15,7]]
#root = [1] ->[[1]] 
#root = [] -> []

#Approach: This is a standard level order traversal (BFS) with a twist: On even levels, add left→right. On odd levels, add right→left.
# Use a queue to traverse each level, as in regular level order.
# For each level, before adding the level’s values to the result, reverse the order if the level is odd-numbered.
