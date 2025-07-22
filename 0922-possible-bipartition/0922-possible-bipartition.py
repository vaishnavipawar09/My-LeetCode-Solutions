class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = [[] for i in range(n+1)]
        for u, v in dislikes:
            adj[u].append(v)
            adj[v].append(u)

        color = [None] * (n+1)

        def dfs(node, c):
            color[node] = c
            for nei in adj[node]:
                if color[nei] is None:
                    if not dfs(nei, 1-c):
                        return False
                elif color[nei] == color[node]:
                    return False
            return True

        for i in range(1, n+1):
            if color[i] is None:
                if not dfs(i, 0):
                    return False
        return True
        

        """
Quick Outline: Coloring Solution (DFS/BFS)
Build an adjacency list for dislikes.
For each uncolored person, start DFS/BFS coloring with color 0.
For each neighbor, if it’s not colored, color it with the opposite color and continue.
If you find a neighbor already colored the same as current, return False.
If you finish without conflict, return True.

Dry Run
Example:
n = 4, dislikes = [[1,2],[1,3],[2,4]]
Build graph: {1: [2,3], 2: [1,4], 3: [1], 4: [2]}
Color mapping: {}

Step-by-step:
Start with node 1, color 0.
color = {1:0}
Neighbor 2: Not colored, dfs(2, 1) color = {1:0, 2:1}
Neighbor 1: already colored (0), OK.
Neighbor 4: Not colored, dfs(4, 0) color = {1:0, 2:1, 4:0}
Neighbor 2: already colored (1), OK.
Done with 4.
Done with 2.
Neighbor 3: Not colored, dfs(3, 1) color = {1:0, 2:1, 4:0, 3:1}
Neighbor 1: already colored (0), OK.
Done with 3.
Continue loop for nodes 2,3,4: already colored.
All checks pass —> return True.

Edge Cases
Disconnected groups: Works, as it checks every node.
No dislikes: Trivially possible, all nodes alone.
Odd cycles: Fails if a cycle of odd length (ex: triangle).
Single person: Trivially possible.
Graph with a self-loop: Not possible, but input guarantees no self-loops.

How to Explain in Interview
Build an adjacency list from dislikes.
Try to 2-color the graph using DFS:
Assign a color to the current node.
For each neighbor, assign the opposite color and continue DFS.
If a neighbor has the same color as the current node, return False.
Handle disconnected graphs by trying to color each unvisited node.
If all checks pass, return True.

Time & Space Complexity
Time: O(N + E), N = people, E = dislikes
Space: O(N + E) for the graph and color dictionary, and recursion stack in the worst case.


"""