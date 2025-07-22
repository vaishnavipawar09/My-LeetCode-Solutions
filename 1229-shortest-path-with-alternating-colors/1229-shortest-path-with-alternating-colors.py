class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in redEdges: 
            graph[a].append((b, "r"))

        for u, v in blueEdges: 
            graph[u].append((v, "b"))

        ans = [-1]*n
        queue = deque([(0, 0, None)])
        visited = set()
        while queue:
            node, dist, prevEdge = queue.popleft()
            visited.add((node, prevEdge))
            if ans[node] == -1:
                ans[node] = dist
            for neighbour, edge in graph[node]:
                if (neighbour, edge) not in visited and prevEdge != edge:
                    queue.append((neighbour, dist+1, edge))
        return ans

"""
How this code works:
Graph Construction: Each node has a list of outgoing edges, and each edge stores its color ("r" or "b").
BFS Traversal: You start BFS from node 0, distance 0, and previous edge as None (so you can take any color for the first move).
    The queue holds (node, dist, prevEdgeColor) tuples.
Visited State: You only revisit a node if you’re coming in with a different last-edge color (so as to allow alternation).
Early Distance Recording: The first time you visit a node (from either color), you set its answer.
Alternation Check: Only enqueue a neighbor if you are not repeating the same color as the previous edge.

Why is this easier?
Single queue (no need to track separate distances for red/blue, since the alternation is handled by prevEdge).
Natural alternation by just comparing prevEdge with the color of the next edge.
Visited set is keyed by (node, color), so you never revisit the same color sequence.
No need for separate answer arrays for red/blue distances—first visit always gives the shortest path.

Dry Run (Example 1):
Input:

n = 3
redEdges = [[0,1],[1,2]]
blueEdges = []
Graph:
0 → [(1, 'r')]
1 → [(2, 'r')]
Start: queue = [(0,0,None)], ans = [-1, -1, -1]
Pop (0, 0, None): mark visited (0, None), ans[0]=0.
Neighbor (1, 'r'), prevEdge!=edge → enqueue (1,1,'r'), mark visited (1, 'r')
Pop (1,1,'r'): mark visited (1,'r'), ans[1]=1.
Neighbor (2, 'r'), prevEdge==edge ('r'=='r') → SKIP, cannot take same color twice.
Queue empty, final ans = [0, 1, -1]

Complexity
Time: O(n + E), like before (each node/edge seen at most twice—once for each color).
Space: O(n + E) for graph, queue, and visited.

Bottom line:
Yes, this is easy and very readable.
It’s slightly less explicit about storing separate distances for red/blue, but it is fine for interviews (and accepted by LeetCode).
If asked about alternate colors for the starting edge, you can clarify that the first move can be either color.
"""
