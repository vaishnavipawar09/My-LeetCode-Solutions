"""
#Method 1: DFS Approach
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

"""

#Method 2: Union Find (mostly used for this) (Optimal)
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # par: parent array, initialized to itself for each node
        par = [i for i in range(n)]
        # rank: size of each component/tree for union by rank
        rank = [1] * n

        # Find function with path compression
        def find(n1):
            res = n1
            # Find the root parent
            while res != par[res]:
                par[res] = par[par[res]]  # Path compression: point to grandparent
                res = par[res]
            return res

        # Union function with union by rank
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)  # Find the parents of both nodes

            if p1 == p2:  # Already connected, no union made
                return 0

            # Attach smaller tree to larger tree
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1  # Union was successful

        # Start with n disconnected components
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)  # Subtract if a union is made

        return res  # Number of connected components

# ----------------------------------------------------
# Implementation Steps (in code comments):

# 1. Initialize parent and rank arrays for n nodes.
# 2. Define 'find' for root finding with path compression.
# 3. Define 'union' for combining two components by rank.
# 4. For each edge, perform union and decrease component count if union occurs.
# 5. Return the count of connected components.

# ----------------------------------------------------
# Dry Run Example

# Input: n = 5, edges = [[0,1],[1,2],[3,4]]
# par = [0,1,2,3,4]
# rank = [1,1,1,1,1]
# res = 5

# Edge [0,1]:
#   find(0) = 0, find(1) = 1 → union possible
#   rank[0] == rank[1], attach 1 to 0, rank[0] = 2
#   par = [0,0,2,3,4], rank = [2,1,1,1,1], res = 4

# Edge [1,2]:
#   find(1) = 0 (since par[1]=0), find(2) = 2
#   union possible: attach 2 to 0, rank[0] = 3
#   par = [0,0,0,3,4], rank = [3,1,1,1,1], res = 3

# Edge [3,4]:
#   find(3)=3, find(4)=4 → union possible, attach 4 to 3, rank[3]=2
#   par = [0,0,0,3,3], rank = [3,1,1,2,1], res = 2

# Final result: 2

# ----------------------------------------------------
# Time Complexity:
# - O(α(n)) per find/union operation (α is the inverse Ackermann function, nearly constant)
# - O(E * α(n)) for E edges (effectively O(E))
# - Total O(n + E)

# Space Complexity:
# - O(n) for parent and rank arrays

# ----------------------------------------------------
