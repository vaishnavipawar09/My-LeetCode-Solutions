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
        