class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # N nodes labeled 1..N, so size N+1 for parent and rank arrays
        N = len(edges)
        par = [i for i in range(N + 1)]    # Parent initialization
        rank = [1] * (N + 1)               # Rank for union by rank

        # Find function with path compression
        def find(n):
            if n != par[n]:
                par[n] = find(par[n])      # Path compression step
            return par[n]

        # Union function with union by rank
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:                   # If parents are the same, cycle detected
                return False

            # Merge lower rank under higher rank
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        # Iterate over each edge and try to union; if union fails, edge is redundant
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]    # Return the redundant edge

# -----------------------------------------------------
# Implementation Steps:
# 1. Initialize parent and rank arrays for all nodes.
# 2. For each edge, perform union.
#    - If union returns False, it means adding this edge forms a cycle (i.e., redundant).
#    - Return that edge immediately.

# -----------------------------------------------------
# Dry Run:
# edges = [[1,2],[1,3],[2,3]]
# par = [0,1,2,3], rank = [1,1,1,1]
# edge [1,2]: union(1,2): parents are 1 and 2 (different). Merge, par[2]=1, rank[1]=2.
# edge [1,3]: union(1,3): find(1)=1, find(3)=3 (different). Merge, par[3]=1, rank[1]=3.
# edge [2,3]: union(2,3): find(2)=1, find(3)=1 (SAME parent), so return [2,3] as redundant.

# -----------------------------------------------------
# Time Complexity:
# - Each union/find operation: O(α(N)), where α is the inverse Ackermann function (almost constant)
# - For E edges: O(E * α(N)), which is O(E) in practice.

# Space Complexity:
# - O(N) for parent and rank arrays.

# -----------------------------------------------------
