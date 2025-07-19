# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:                         # Handle base case if tree is empty      O(1)
            return []

        res = []                             # List to store result                   O(1)
        q = collections.deque()              # Initialize queue for BFS
        q.append(root)                       # Start with the root node

        while q:                             # While queue not empty, traverse tree
            level = []                       # Temp list to collect values for this level
            for _ in range(len(q)):          # Traverse current level (O(n) total for all nodes)
                node = q.popleft()           # Pop from queue (FIFO)                 O(1)
                level.append(node.val)       # Add node value to current level        O(1)
                if node.left:                # Add children to queue for next level   O(1)
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)                # Append current level to result         O(1)
        
        return res[::-1]                     # Reverse the result for bottom-up order O(n)


#Time Complexity: O(n)
#The outer while q loop runs once for every node in the tree.
#The inner for loop traverses all nodes across all levels — each node is processed exactly once.
#res[::-1] reverses the list of levels at the end, which is O(n) for n nodes.
#Total: O(n) + O(n) = O(n)

#Space Complexity: O(n)
#The queue (q) at most holds one level of nodes at a time (up to O(n) in the worst case).
#The result list (res) holds every node once (O(n)).  Total: O(n)

"""Step-by-step BFS Process
Start:Queue: [3] Result: []
# Level 1: Nodes at this level: 1 (only 3) Pop 3 from queue → Add value 3 to level list: [3]
#Add children of 3:  Left child 9 → queue: [9] Right child 20 → queue: [9, 20] Add [3] to result: [[3]]
#Level 2: Nodes at this level: 2 (9, 20) Pop 9 → Add value 9 to level: [9] 9 has no children Pop 20 → Add value 20 to level: [9, 20] 
#Add 20's children: Left child 15 → queue: [15] Right child 7 → queue: [15, 7] Add [9, 20] to result: [[3], [9, 20]]
# Level 3: Nodes at this level: 2 (15, 7) Pop 15 → Add value 15 to level: [15] (no children) Pop 7 → Add value 7 to level: [15, 7] (no children) Add [15, 7] to result: [[3], [9, 20], [15, 7]]
#Queue is empty: BFS complete Result (top-down): [[3], [9, 20], [15, 7]]
# Reverse for bottom-up: Final output: [[15, 7], [9, 20], [3]]"""



#Clarifying questions:
#Is the input always a valid binary tree (no cycles)?
#Will the input be a TreeNode structure (not an array/list)?
#What should I return if the tree is empty? (Return [])
#Can node values be negative or duplicated?
#Is the bottom-up strictly from leaf level to root level?

#root = [3,9,20,null,null,15,7] → Output: [[15,7],[9,20],[3]]
#root = [1] → Output: [[1]]
#root = [] → Output: []

#Approach:
#This is a classic level-order (BFS) traversal, but you collect each level's node values in a result list.
#At the end, reverse the result so the output is from bottom to top.