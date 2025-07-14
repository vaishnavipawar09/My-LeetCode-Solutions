class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Given a grid with walls (-1), gates (0), and empty rooms (INF),
        fill each empty room with the distance to its nearest gate.
        Walls remain -1. Gates remain 0. In-place update.
        """

        rows, cols = len(rooms), len(rooms[0])
        visited = set()         # Track visited positions
        q = deque()             # BFS queue: holds positions to process

        # Implementation Step 1: Helper function to add a room to the queue if it is valid
        def addRoom(r, c):
            # Ignore out-of-bounds, already visited, or wall cells
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                (r, c) in visited or rooms[r][c] == -1):
                return 
            visited.add((r, c))      # Mark as visited
            q.append((r, c))         # Add to queue

        # Implementation Step 2: Enqueue all gates (cells with value 0)
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        dist = 0   # Current distance from the nearest gate

        # Implementation Step 3: Multi-source BFS, level by level
        while q: 
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist   # Update room's distance
                # Add all 4 neighbors
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            dist += 1   # After each level, increase distance by 1

        
        
# -------------------------------------------
        # Dry Run (inline for an example):
        # Input: rooms = [
        #   [INF, -1, 0, INF],
        #   [INF, INF, INF, -1],
        #   [INF, -1, INF, -1],
        #   [0, -1, INF, INF]
        # ]
        #
        # 1. Enqueue all gates: positions (0,2) and (3,0)
        # 2. BFS step 1 (dist=0): these are gates, set to 0 (already are)
        # 3. BFS step 2 (dist=1): add valid neighbors (0,3), (1,2), (2,0), set to 1
        # 4. BFS step 3 (dist=2): from new frontier, add their neighbors not visited, set to 2
        # ... and so on until all reachable rooms filled with min distance to a gate.
        # -------------------------------------------

        # Complexity Analysis:
        # Time Complexity: O(m * n), where m is rows, n is cols, since each cell is visited once
        # Space Complexity: O(m * n) for the queue and visited set (worst case: all empty rooms)
