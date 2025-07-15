class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Step 1: Handle base case (empty graph)
        if not n:
            return True  # No nodes is technically a tree

        # Step 2: Build adjacency list for undirected graph
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        # Step 3: DFS to check for cycles and ensure all nodes are connected
        visit = set()  # keep track of visited nodes

        def dfs(i, prev):
            if i in visit:
                return False  # Cycle detected!
            visit.add(i)
            for j in adj[i]:
                if j == prev:  # Don't go back to parent node
                    continue
                if not dfs(j, i):
                    return False
            return True  # No cycle found

        # Step 4: Must satisfy two conditions for a valid tree:
        # 1. Connected: all nodes are visited from node 0 (len(visit) == n)
        # 2. No cycles: DFS returns True (never revisited a node)
        return dfs(0, -1) and n == len(visit)

        # -------------------------
        # Implementation Steps:
        # 1. Build an adjacency list for all n nodes.
        # 2. Run DFS from node 0, passing the previous node to avoid trivial cycles.
        # 3. If DFS returns False, a cycle was found → not a tree.
        # 4. After DFS, check if the number of visited nodes is exactly n (the graph is fully connected).
        #    - If not all nodes are visited, the graph is disconnected → not a tree.
        # 5. If both checks pass, return True; else, return False.

        # -------------------------
        # Dry Run Example:
        # n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
        # adj = {0: [1,2,3], 1: [0,4], 2: [0], 3: [0], 4: [1]}
        # Start DFS(0, -1):
        #   - visit = {0}
        #   - check 1: j=1 → DFS(1, 0): visit = {0,1}
        #     - check 1: j=0 (parent, skip)
        #     - check 2: j=4 → DFS(4,1): visit={0,1,4} (ends)
        #   - check 2: j=2 → DFS(2,0): visit={0,1,4,2}
        #   - check 3: j=3 → DFS(3,0): visit={0,1,4,2,3}
        # All nodes visited, no cycles, returns True.

        # -------------------------
        # Time Complexity: O(N + E)
        # - Each node and edge visited once
        #   - N = number of nodes, E = number of edges

        # Space Complexity: O(N)
        # - For adjacency list and visited set
        # - DFS recursion stack up to O(N) in worst case (tree)
