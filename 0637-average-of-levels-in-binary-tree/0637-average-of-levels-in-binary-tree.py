# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:                    # Handle edge case: empty tree (not needed for this problem, but good practice)
            return []

        res = []                        # Final result: list of averages for each level
        q = collections.deque([root])   # Initialize queue for BFS, start with root

        while q:                        # While there are nodes to process
            level = []                  # Collect node values for this level
            for _ in range(len(q)):     # Process all nodes at current level
                node = q.popleft()
                level.append(node.val)
                if node.left:           # Add left child if exists
                    q.append(node.left)
                if node.right:          # Add right child if exists
                    q.append(node.right)

            res.append(sum(level)/len(level))  # Calculate average for this level, append to result

        return res


"""Time & Space Complexity
Time: O(n)
Each node is visited exactly once.
Calculating sum(level) is O(k) per level, but over all levels, every node is summed once → O(n) total.

Space: O(n)
At worst, the queue holds all nodes at the widest level (O(n)).
The result list stores one float per level (≤ n).

Step-by-step BFS Dry Run (Comments Style)
Input:
root = [3,9,20,null,null,15,7]

Tree:
      3
    /   \
   9     20
        /  \
      15    7
Start: queue = [3], result = []
Level 1:queue length = 1 pop 3 → level = [3] add children: 9, 20 → queue = [9, 20] average = 3 / 1 = 3.0 result = [3.0]
Level 2:queue length = 2 pop 9 → level = [9], pop 20 → level = [9, 20] add children: 20 → left(15), right(7): queue = [15, 7]
average = (9+20) / 2 = 14.5 result = [3.0, 14.5]
Level 3: queue length = 2  pop 15 → level = [15], pop 7 → level = [15, 7] no children to add (queue empty)
average = (15+7) / 2 = 11.0 result = [3.0, 14.5, 11.0]
Output: [3.0, 14.5, 11.0]

Clarifying Questions
#Is the input always a valid binary tree? (Assume yes, per constraints)
#Are negative and large values allowed? (Yes, as per constraints)
What if the tree has only one node? (Return single average)
Should the result be floats? (Yes, per the problem)
How accurate? (Within 1e-5 is enough)

Sample Test Cases
root = [3,9,20,null,null,15,7] → [3.0, 14.5, 11.0]
root = [3,9,20,15,7] → [3.0, 14.5, 11.0]
root = [1] → [1.0]


Approach Statement (to remember):
"Do a level order BFS, collect all node values at each level, then take their average."
"""
