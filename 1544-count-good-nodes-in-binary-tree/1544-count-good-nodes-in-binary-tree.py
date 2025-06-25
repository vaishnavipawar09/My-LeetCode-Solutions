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

#Time Complexity: O(n)
#Space Complexity : O(1)