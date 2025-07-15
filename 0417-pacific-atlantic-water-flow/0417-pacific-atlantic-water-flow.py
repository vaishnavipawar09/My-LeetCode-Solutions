class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Step 1: Get grid dimensions
        ROWS, COLS = len(heights), len(heights[0])
        
        # Step 2: Create two sets to track cells reachable by Pacific and Atlantic
        pac, atl = set(), set()  # Pacific (top, left) and Atlantic (bottom, right)
        
        # Step 3: DFS helper to mark reachable cells
        def dfs(r, c, visit, prevHeight):
            # Base case: out of bounds, already visited, or height decreases (cannot flow)
            if (
                (r, c) in visit or 
                r < 0 or c < 0 or 
                r == ROWS or c == COLS or 
                heights[r][c] < prevHeight
            ):
                return
            visit.add((r, c))  # Mark as visited
            
            # Explore 4 directions
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # Step 4: Start DFS from all Pacific edges (top row and left column)
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])          # Top edge
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])  # Bottom edge
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])          # Left edge
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])  # Right edge

        # Step 5: Collect cells that can reach both oceans
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res

        
        # --- Time Complexity ---
        # O(m * n), where m = #rows, n = #cols.
        #   - Each cell is visited at most twice (once from Pacific, once from Atlantic).

        # --- Space Complexity ---
        # O(m * n) for recursion stack (worst case all land is accessible), and two sets for visited tracking.

        # --- Implementation Steps ---
        # 1. Use DFS to find all cells that can flow to the Pacific and Atlantic oceans independently.
        # 2. For Pacific: Start from top row and left column, marking all cells you can reach by going "uphill".
        # 3. For Atlantic: Start from bottom row and right column, marking all cells you can reach by going "uphill".
        # 4. The answer is cells that can be reached from *both* DFS traversals (intersection of the two sets).

        # --- Dry Run Example ---
        # Input: heights = [
        #   [1,2,2,3,5],
        #   [3,2,3,4,4],
        #   [2,4,5,3,1],
        #   [6,7,1,4,5],
        #   [5,1,1,2,4]
        # ]
        # - Cells at edges flow to their respective oceans.
        # - Cells where water can flow to both top/left and bottom/right edges (e.g. (0,4), (1,3), (1,4), (2,2), (3,0), (3,1), (4,0)) are added to the result.


        