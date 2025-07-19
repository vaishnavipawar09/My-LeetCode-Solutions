# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = collections.deque()     # Initialize the queue for BFS traversal.
        q.append([root, root.val])  # Each queue element is [node, max value seen so far in the path]
        good = 0                    # Counter for good nodes

        while q:                    # While queue is not empty
            node, maxval = q.popleft()  # Get the node and the max value so far
            if node.val >= maxval:  # Each queue element is [node, max value seen so far in the path]
                good += 1           # it is a good node (no ancestor is greater than it on the path)

            # For each child, add them to the queue with updated max-so-far
            # Always carry forward the largest value seen so far in the path
            if node.left:
                q.append([node.left, max(maxval, node.val)])
            if node.right:
                q.append([node.right, max(maxval, node.val)])

        return good    # Return total number of good nodes found

#Dry Run (Example 1)
#Tree: [3,1,4,3,null,1,5]
"""
       3
      / \
     1   4
    /   / \
   3   1   5
Start at root (3): max_so_far = 3, good = 1
Left child (1): max_so_far = 3, 1 < 3 → not good
Left child (3): max_so_far = 3, 3 == 3 → good
Right child (4): max_so_far = 3, 4 > 3 → good
Left child (1): max_so_far = 4, 1 < 4 → not good
Right child (5): max_so_far = 4, 5 > 4 → good
Total good nodes: 1 (root) + 1 (left-3) + 1 (4) + 1 (5) = 4

How to Remember
“DFS the tree, passing the max seen so far. If a node is at least as large as all its ancestors, it’s a good node.”
"""
#Time Complexity: O(n)      Each node is visited once.
#Space Complexity : O(n)    Recursion stack is at most the height of the tree. Worst-case O(n) (skewed), best-case O(log n) (balanced).


#Clarifying Questions
#Can the binary tree have negative values? (Yes)
#Can node values be duplicated? (Yes)
#Is the input always a valid binary tree (no cycles)? (Yes)
#Will the input be given as a TreeNode class? (Yes)
#What should I return if the tree is empty? (Return 0, but constraints say at least 1 node.)


#Approach
#This is a classic tree DFS/BFS problem:
#For each node, keep track of the maximum value seen so far from the root to that node.
#If the node’s value is greater than or equal to this max, it’s a good node.
#Recursively visit all nodes (DFS—preorder is simplest), passing the updated max-so-far.
#Count and return the total number of good nodes.



#[3,1,4,3,null,1,5] → 4
#[3,3,null,4,2] → 3