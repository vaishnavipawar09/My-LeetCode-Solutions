"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}  # Hashmap to keep track of cloned nodes: {original_node: cloned_node}

        def dfs(node):
            # If the node has already been cloned, return its clone (prevents cycles/infinite recursion)
            if node in oldToNew:
                return oldToNew[node]

            # Clone the current node (but neighbors will be filled next)
            copy = Node(node.val)
            oldToNew[node] = copy  # Add to the map before recursive calls

            # Recursively clone all neighbors and add them to the neighbors of the clone
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None  # Handle empty input

#Time and Space Complexity
# Time Complexity: O(N), where N is the number of nodes. Each node and edge is visited/cloned once.
# Space Complexity: O(N), for the recursion stack and the oldToNew hashmap.

#Implementation Steps (as comments):
# 1. Handle empty graph: If input node is None, return None.
# 2. Create a hash map: oldToNew maps original nodes to their clones.
# 3. Define DFS helper:
#   If node already cloned, return its clone.
#   Clone the node and store it in the map.
#   Recursively clone all neighbors and add to the cloned node’s neighbors list.
# 4. Start DFS: Return the clone of the starting node.

# Example graph:
# 1 -- 2
# |    |
# 4 -- 3

# Let’s say the starting node is 1.
# - oldToNew = {}
# Call dfs(1):
#   - 1 not in oldToNew: create copy1, oldToNew[1] = copy1
#   - for neighbor 2:
#       - dfs(2)
#           - 2 not in oldToNew: create copy2, oldToNew[2]=copy2
#           - for neighbor 1: (back edge)
#               - dfs(1) → already in oldToNew, return copy1
#           - for neighbor 3:
#               - dfs(3)
#                   - 3 not in oldToNew: create copy3, oldToNew[3]=copy3
#                   - for neighbor 2: dfs(2) → already cloned, return copy2
#                   - for neighbor 4:
#                       - dfs(4)
#                           - 4 not in oldToNew: create copy4, oldToNew[4]=copy4
#                           - for neighbor 1: dfs(1) → already cloned, return copy1
#                           - for neighbor 3: dfs(3) → already cloned, return copy3
#                       - copy4.neighbors = [copy1, copy3]
#                   - copy3.neighbors = [copy2, copy4]
#           - copy2.neighbors = [copy1, copy3]
#   - for neighbor 4:
#       - dfs(4) → already in oldToNew, return copy4
# - copy1.neighbors = [copy2, copy4]
# Returns copy1 (full deep copy graph)
