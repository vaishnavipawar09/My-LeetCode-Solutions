#clarifying questions:
#Can oranges rot diagonally? no
#is an empty cell(0c) traversal? no
#should we return -1 if any fresh oragane is unreachable? yes

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 1. Initialize variables and helper data
        rows, cols = len(grid), len(grid[0])          # Grid dimensions
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]] # 4-neighbor directions
        fresh = 0                                     # Counter for fresh oranges
        q = deque()                                   # Queue for BFS

        # 2. Scan the grid to initialize the queue and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))     # Add all rotten oranges to the queue
                elif grid[r][c] == 1:
                    fresh += 1           # Count all fresh oranges

        time = 0    # Tracks minutes elapsed

        # 3. BFS: For each minute, process all rotten oranges currently in the queue
        while q and fresh > 0:
            for i in range(len(q)):   # Only process oranges that are rotten at the current minute
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # 4. If neighbor is in bounds and is a fresh orange, rot it and add to queue
                    if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1):
                        grid[nr][nc] = 2       # Make the fresh orange rotten
                        fresh -= 1             # One less fresh orange
                        q.append((nr, nc))     # Add new rotten orange to queue for next minute
            time += 1      # Finished one minute (one BFS level)

        # 5. Return result
        return time if fresh == 0 else -1   # If all fresh rotted, return time; else, -1

        # Implementation Steps:
        # - Start by putting all rotten oranges in the queue (multi-source BFS)
        # - For each minute, rot all adjacent fresh oranges, update queue
        # - Track how many minutes passed and how many fresh oranges are left
        # - Stop when no fresh oranges remain or no more can be rotted

        # Time Complexity: O(m * n)
        #   (Each cell is visited at most once)
        # Space Complexity: O(m * n)
        #   (Queue could store all oranges in the worst case)

        # Dry Run Example:
        # Input: grid = [
        #   [2,1,1],
        #   [1,1,0],
        #   [0,1,1]
        # ]
        # Start: fresh=6, q=[(0,0)]
        # Minute 1: rot (0,1), (1,0)
        # Minute 2: rot (0,2), (1,1)
        # Minute 3: rot (2,1)
        # Minute 4: rot (2,2)
        # End: fresh=0, time=4 → Output: 4

        # If any fresh orange cannot be reached, e.g. surrounded by walls, returns -1

        #“Start BFS from all rotten oranges. For each minute, rot all adjacent fresh oranges. Count minutes. If any fresh left at the end, return -1.”