class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}

        def dfs(node):
            if node in safe:
                return safe[node]
            safe[node] = False
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            safe[node] = True
            return safe[node]

        res = []
        for node in range(n):
            if dfs(node):
                res.append(node)
        return res

"""
Clarifying Questions
Are nodes always labeled 0 to n-1?
Yes.

Can there be cycles and self-loops?
Yes, both are possible.

Should the output be sorted?
Yes, return the safe nodes sorted in ascending order.

Is the input always a valid directed graph?
Yes.

Time & Space Complexity
Time: O(V + E) — Each node and edge is processed at most once.

Space: O(V + E) for the graph and bookkeeping.

Dry Run (Example 1)
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Nodes 5, 6 are terminal (no outgoing edges).
Node 2 points to 5 (safe) — so 2 is safe.
Node 4 points to 5 — so 4 is safe.
Node 0 → 1/2; node 1 → 2/3; node 3 → 0 (cycle).
Safe nodes: [2, 4, 5, 6].

Approach:
Create a hashmap to keep a track of whch nodes are safe and which nodes are unsafe, start from the start node, and run dfs on its nei as well

"""