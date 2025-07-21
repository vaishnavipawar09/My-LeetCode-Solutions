class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nr, nc = row +dr, col +dc
                    if (nr in range(rows) and nc in range(cols) and grid[nr][nc] == "1" and (nr, nc) not in visited):
                        visited.add((nr, nc))
                        q.append((nr, nc))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands


"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0                       # Edge case: If grid is empty, return 0

        rows, cols = len(grid), len(grid[0])   # Get number of rows and columns
        visit = set()                      # Set to keep track of visited cells (r, c)
        islands = 0                        # Counter for number of islands found

        def bfs(r, c):                     # BFS to visit all cells in the current island
            q = deque()                    # Create a queue for BFS
            visit.add((r, c))              # Mark starting cell as visited
            q.append((r, c))               # Add starting cell to queue

            while q:
                row, col = q.popleft()     # Pop cell from front of queue
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]   # Down, Up, Right, Left
                for dr, dc in directions:  # For all 4 directions
                    nr, nc = row + dr, col + dc  # Calculate neighbor cell position
                    # Check if neighbor is in bounds, is land, and not visited
                    if (nr in range(rows) and nc in range(cols) and 
                        grid[nr][nc] == "1" and (nr, nc) not in visit):
                        q.append((nr, nc))     # Add neighbor to queue
                        visit.add((nr, nc))    # Mark neighbor as visited

        # Go through every cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If cell is land and not yet visited, it's a new island
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)            # Perform BFS to mark the whole island
                    islands += 1         # Increment island count

        return islands                   # Return total number of islands

# Complexity:
# Time Complexity: O(m * n), where m = rows and n = columns.
#   - Each cell is processed once, either marked as visited or ignored.
# Space Complexity: O(m * n) in the worst case.
#   - The queue and visited set may both grow to hold all grid cells (if all land).

# Dry Run Example:
# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]                         output: 3 islands

# Step-by-step walkthrough:
# Loop: r = 0, c = 0
# - grid[0][0] == "1" and (0,0) not in visit → Start BFS (islands = 1)
#   BFS visits (0,0), (1,0), (0,1), (1,1), all marked visited.
# Loop: r = 0, c = 1
# - grid[0][1] == "1" but already in visit → skip
# Continue... All cells in the first island are already visited.
# Loop: r = 2, c = 2
# - grid[2][2] == "1" and (2,2) not in visit → Start BFS (islands = 2)
#   BFS only visits (2,2).
# Loop: r = 3, c = 3
# - grid[3][3] == "1" and (3,3) not in visit → Start BFS (islands = 3)
#   BFS visits (3,3), (3,4) as both are "1".
# End of loops.
# Return islands → 3

# The function correctly finds 3 islands.

# Implementation Steps in short
# 1. Edge Case: If the grid is empty, return 0.
# 2. Initialization: Store the number of rows and columns. Create a set to track visited cells. Initialize the island count to 0.
# 3. BFS Traversal: Define a bfs function that: Adds the starting cell to the queue and marks as visited.
#    For each cell, explores its 4 neighbors (up, down, left, right). If a neighbor is land, within bounds, and not visited, add to queue and mark as visited.
# 4. Iterate Over Grid: For every cell: If the cell is land ('1') and not visited, it's a new island. Call bfs to visit the entire island. Increment the island count.
# 5. Return Result: Return the total number of islands found.

#implemenataion in short 
# 1. Iterate over every cell in the grid.
# 2. If cell is land and not visited, run BFS from there to visit the entire island.
# 3. Use a visited set to ensure no land cell is counted more than once.
# 4. Count how many times BFS is started; this is the number of islands.

#Clarifying questions:
#1. Can i move diagonally ? No
#
  """      