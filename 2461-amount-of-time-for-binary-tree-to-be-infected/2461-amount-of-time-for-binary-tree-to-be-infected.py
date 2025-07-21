# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # Step 1: Build parent map and find start node
        parent = {}
        node_map = {}

        def dfs(node, par=None):
            if node:
                node_map[node.val] = node
                parent[node] = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        start_node = node_map[start]

        # Step 2: BFS from start node
        visited = set()
        q = deque([start_node])
        visited.add(start_node)
        time = -1   # We start from -1 because the last increment happens after last infection

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for neighbor in [node.left, node.right, parent[node]]:
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
            time += 1

        return max(time, 0)

        
#Time: O(n) — Every node is visited once for parent map and once for BFS.
#Space: O(n) — Parent map, node map, queue, and visited set.


"""
Step 1: Clarifying Questions
Are all node values unique? Yes (per constraints).
Is the input always a valid binary tree and does it always contain the start value? Yes.
Can the infection spread both to children and the parent? (i.e., does adjacency include parent?)
Yes (implied, otherwise some nodes would never get infected).

Step 2: Approach & Explanation
Key Idea
Infection spreads bidirectionally: from a node to its children and to its parent.
The tree is unidirectional (parent to child), so to traverse up (to parent), you must build a parent map.
The process is similar to BFS (level-order traversal): each minute, infect all adjacent (uninfected) nodes.
The time required is the maximum distance from the start node to any other node in the tree.

Implementation Plan
1. Build Parent Map:
Traverse the tree and record the parent for every node (using DFS or BFS).
2. Locate the Start Node:
Find the TreeNode with value start (can be done while building parent map).
3. BFS from Start Node:
At each level/minute, infect all uninfected neighbors (left, right, parent).
4. Count Levels:
The number of BFS levels to reach all nodes = answer.

Step 5: Dry Run (Example 1)
Tree: [1,5,3,null,4,10,6,9,2], start=3
Minute 0: {3}
Minute 1: {1, 10, 6} (neighbors of 3)
Minute 2: {5} (neighbor of 1)
Minute 3: {4} (neighbor of 5)
Minute 4: {9, 2} (neighbors of 4)

Total time: 4
"""