class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list for the undirected graph
        adj = [[] for _ in range(n)]    # O(n) space
        visit = [False] * n             # Visited flag for each node, O(n) space
        for u, v in edges:              # O(E) time
            adj[u].append(v)
            adj[v].append(u)

        # DFS function to mark all nodes in this component as visited
        def dfs(node):
            for nei in adj[node]:        # For all neighbors
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        
        res = 0
        for node in range(n):           # For every node in the graph
            if not visit[node]:         # If node is not visited, it's a new component
                visit[node] = True      # Mark as visited
                dfs(node)               # Visit all nodes in this component
                res += 1                # Increment component count
        return res

# ----------------------------------------------------
# Implementation Steps (in comments):

# 1. Build adjacency list 'adj' from the edge list.
# 2. Initialize a visited list of size n (all False).
# 3. Define a DFS function that marks all connected nodes as visited.
# 4. Iterate through all nodes:
#     - If the node hasn't been visited, it's a new component.
#     - Run DFS from this node to mark all connected nodes.
#     - Increment the component counter.
# 5. Return the total number of components found.

# ----------------------------------------------------
# Dry Run Example

# Input: n = 5, edges = [[0,1],[1,2],[3,4]]
# adj = [[1], [0,2], [1], [4], [3]]
# visit = [False, False, False, False, False]
# res = 0

# node = 0: not visited → visit[0]=True, dfs(0) visits 1, 2
#     After dfs: visit = [True, True, True, False, False], res = 1

# node = 1: already visited, skip
# node = 2: already visited, skip
# node = 3: not visited → visit[3]=True, dfs(3) visits 4
#     After dfs: visit = [True, True, True, True, True], res = 2

# node = 4: already visited, skip

# Output: 2

# ----------------------------------------------------
# Time Complexity: 
# - O(n + E): Each node and each edge is visited at most once.

# Space Complexity:
# - O(n + E): For adjacency list (O(E)), visited array (O(n)), and recursion stack (up to O(n) in worst case).

