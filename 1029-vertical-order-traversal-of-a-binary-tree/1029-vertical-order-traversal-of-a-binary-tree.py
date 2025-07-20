# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        col_table = defaultdict(list)       # # {col: [(row, val), ...]}
        queue = deque([(root, 0, 0)])         # (node, row, col)

        while queue:
            node, row, col = queue.popleft()
            if node:
                col_table[col].append((row, node.val))  #append the row and the value in the col dict
                queue.append((node.left, row +1, col -1))
                queue.append((node.right, row + 1, col +1))

        res = []
        for col in sorted(col_table.keys()):        #leftmost col to rightmost col
            #sort by the row first and then the value
            level = sorted(col_table[col], key = lambda x: (x[0], x[1]))
            res.append([val for row, val in level])
        
        return res

"""
Time and Space Complexity (Line-by-Line)
BFS Traversal: Every node is visited once, so O(n) for n nodes.
Appending to col_table: Each append is O(1), total O(n).
Sorting columns: There are at most n unique columns, each with up to n nodes:
The total number of nodes to sort over all columns is n, so sorting is O(n log n).
Final extraction: Linear in the number of nodes, O(n).
Space: O(n) for storing col_table, and O(n) for queue.

So:
Time Complexity: O(n log n) (for the sorting step).
Space Complexity: O(n).

Dry Run (for Example 1: [3,9,20,null,null,15,7])
Tree:

      3
     / \
    9   20
        / \
      15   7
Positioning:
(0,0): 3
(1,-1): 9
(1,1): 20
(2,0): 15
(2,2): 7

BFS order:
queue: [(3, 0, 0)] → pop 3: col_table[0] = [(0,3)], queue: [(9,1,-1),(20,1,1)]
pop 9: col_table[-1] = [(1,9)], queue: [(20,1,1)]
pop 20: col_table[1]=[(1,20)], queue: [(15,2,0),(7,2,2)]
pop 15: col_table[0] = [(0,3),(2,15)], queue: [(7,2,2)]
pop 7: col_table[2]=[(2,7)], queue: []

Column Groups:
-1: [(1,9)]
0: [(0,3),(2,15)]
1: [(1,20)]
2: [(2,7)]

Final output (extract by sorted col, row, val): [[9], [3, 15], [20], [7]]

"""

#Are all node values unique? (Not required, but clarifies sort order)
#Can the tree be empty? (Yes, return [])
#Do we need to sort by value if nodes share row and col? (Yes)
#Can nodes have negative or very large values? (Yes, but no special handling)
#Input is always a valid binary tree?

"""
Intuition & Approach
Vertical order traversal means grouping tree nodes by their column index, from leftmost to rightmost.
Positioning:
Root is at (row=0, col=0).
Left child: (row+1, col-1)
Right child: (row+1, col+1)

Rules:
For each column, nodes must be reported from top to bottom.
If nodes are in the same row and column, sort them by their values.
So, we need to:
Traverse all nodes, collecting (col, row, value) for each node.
Group nodes by col.
For each column, sort the nodes by (row, value).

Step-by-step Algorithm
Use BFS (queue) or DFS (recursion) to traverse the tree.
For each node, record: (col, row, value).
Store nodes by column in a dictionary: col_table[col] = list of (row, value).
After traversal:
Sort columns by increasing col.
For each column, sort entries by (row, value), extract values, and return them as a list.

"""