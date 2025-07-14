#DFS Approach : recursion
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Edge case: If grid is empty, return 0 (no islands)
        if grid is None:
            return 0

        rows, cols = len(grid), len(grid[0])       # Get dimensions of the grid
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # 4-directional movement
        visit = set()                              # Set to keep track of visited cells

        def dfs(r, c):
            # If out of bounds, water cell, or already visited, stop recursion
            if (r < 0 or r >= rows or c < 0 or c >= cols or 
                grid[r][c] == 0 or (r, c) in visit):
                return 0

            visit.add((r, c))  # Mark cell as visited

            # Recursively visit all neighbors and accumulate area
            return (1 + 
                    dfs(r+1, c) + 
                    dfs(r-1, c) + 
                    dfs(r, c+1) + 
                    dfs(r, c-1))

        area = 0  # Track the maximum island area found

        # Traverse every cell in the grid
        for r in range(rows):
            for c in range(cols):
                # Start DFS if unvisited land is found
                if grid[r][c] == 1 and (r, c) not in visit:
                    area = max(area, dfs(r, c))  # Update maximum area if larger island found

        return area  # Return the largest island area

        # Implementation Steps:
        # 1. For each cell, if it's land (1) and not visited, run DFS.
        # 2. In DFS, mark visited and explore all four directions.
        # 3. Sum the area of the current island recursively.
        # 4. Keep track of the largest area encountered.
        # 5. Return the maximum area at the end.

        # Time Complexity: O(m * n)
        #   - Each cell is visited at most once.
        # Space Complexity: O(m * n)
        #   - In the worst case (all land), the recursion stack and visited set
        #     will be size O(m * n), where m and n are the grid dimensions.

# Dry Run Example:

# grid = [
#   [0,0,1,0],
#   [1,1,1,0],
#   [0,0,0,1]
# ]
#
# Step-by-step:
# - (0,2) is land and not visited: start DFS, area = 1
#   - (1,2) is land, area += 1 (total 2)
#     - (1,1) is land, area += 1 (total 3)
#       - (1,0) is land, area += 1 (total 4)
#     - (1,3), (2,1), etc. are not land or already visited.
# - (1,0), (1,1), (1,2) are already visited.
# - (2,3) is land and not visited: start DFS, area = 1
# - No more unvisited land.
# - Return max area = 4



"""
#BFS Approach : Iterative
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if grid is None:
            return 0

        rows, cols = len(grid), len(grid[0])
        area = 0
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))
            curr_area = 1

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if(nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 0 or (nr, nc) in visited):
                        continue

                    visited.add((nr,nc))
                    q.append((nr,nc))
                    curr_area  += 1
            return curr_area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = max(area, bfs(r, c))
        return area

"""