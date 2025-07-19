# Definition for a Node.
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children if children is not None else []

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:                   # Handle edge case: empty tree. O(1)
            return []

        res = []                       # Final result: list of lists. O(1)
        q = collections.deque([root])  # Queue for BFS, initialized with root. O(1)

        while q:                       # While queue not empty (process all nodes). O(n)
            level = []                 # Temp list for current level's node values.
            for _ in range(len(q)):    # Process each node in the current level.
                node = q.popleft()     # Pop node from left. O(1)
                level.append(node.val) # Record value. O(1)
                for child in node.children:  # Enqueue all children.
                    q.append(child)    # Add child to queue. O(1) per child, total O(n)
            res.append(level)          # Add the level's values to result. O(1)

        return res


#Time: O(n)
#Each node is visited/processed exactly once (in both while and inner for).
#Enqueue and dequeue each node once.
#Appending children: Each edge in the tree is traversed once.
#Building the final result: O(n) for all nodes.

#Space: O(n)
#The queue can hold up to O(n) nodes at the widest level. The result list stores all nodes’ values (O(n)).
#No extra recursion stack (unlike DFS).

#Clarifying Questions:
#Is the input always a valid N-ary tree (no cycles/duplicates)?
#Will the input be a Node object, not a list/array? (Assumed Node)
#What should I return if the tree is empty? ([])
#Can node values be negative or duplicated?
#Is there a max number of children per node? (Assume any, since N-ary)

#Test Cases:
#root = [1, null, 3, 2, 4, null, 5, 6] Output: [[1], [3,2,4], [5,6]]
#root = [] Output: []
#root = [1] Output: [[1]]

#"Traverse the N-ary tree using BFS: for each level, collect the node values, and enqueue all children for the next level."

"""Step-by-step BFS Dry Run
Example Input:
root = [1, null, 3, 2, 4, null, 5, 6]

Visual tree:

markdown
Copy
Edit
      1
    / | \
   3  2  4
  / \
 5   6
Start:

Queue: [1]

Result: []

Level 1:

Queue length = 1

Pop 1 → level = [1]

Children of 1: 3, 2, 4 → queue: [3, 2, 4]

Add [1] to result → [[1]]

Level 2:

Queue length = 3

Pop 3 → add 3 to level: [3]

Children of 3: 5, 6 → queue: [2, 4, 5, 6]

Pop 2 → add 2: [3, 2] (no children)

Pop 4 → add 4: [3, 2, 4] (no children)

Add [3, 2, 4] to result → [[1], [3, 2, 4]]

Level 3:

Queue length = 2

Pop 5 → add 5: [5] (no children)

Pop 6 → add 6: [5, 6] (no children)

Add [5, 6] to result → [[1], [3, 2, 4], [5, 6]]

Done. Queue empty. Output:

[[1], [3, 2, 4], [5, 6]]

"""