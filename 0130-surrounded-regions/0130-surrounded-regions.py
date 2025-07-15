class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Step 1: Get the dimensions of the board
        ROWS, COLS = len(board), len(board[0])

        # Helper function: Mark all 'O's connected to (r, c) with 'T' (temporary)
        def capture(r, c):
            # If out of bounds or not 'O', stop
            if (r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O"):
                return
            board[r][c] = "T"      # Mark current cell as temporary
            # Visit all 4 neighbors
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # ----------------------------------------------------------------------
        # Implementation Steps:

        # 1. Traverse all border cells; for each border 'O', use DFS to mark all
        #    connected 'O's as 'T' (these are NOT surrounded regions).
        for r in range(ROWS):
            for c in range(COLS):
                # Only process border cells with 'O'
                if (board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1])):
                    capture(r, c)

        # 2. Traverse the whole board; change all unmarked 'O's (truly surrounded)
        #    to 'X' (capture), since they weren't connected to the border.
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # 3. Change all 'T's back to 'O' (restore the border-connected regions).
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"

        # ----------------------------------------------------------------------
        # Dry Run Example:
        #
        # Input board:
        # [
        #   ["X","X","X","X"],
        #   ["X","O","O","X"],
        #   ["X","X","O","X"],
        #   ["X","O","X","X"]
        # ]
        #
        # 1. Mark border-connected 'O's (only cell at [3,1]):
        #      ["X","X","X","X"]
        #      ["X","O","O","X"]
        #      ["X","X","O","X"]
        #      ["X","T","X","X"]
        #
        # 2. Convert surrounded 'O's to 'X':
        #      ["X","X","X","X"]
        #      ["X","X","X","X"]
        #      ["X","X","X","X"]
        #      ["X","T","X","X"]
        #
        # 3. Restore 'T' to 'O':
        #      ["X","X","X","X"]
        #      ["X","X","X","X"]
        #      ["X","X","X","X"]
        #      ["X","O","X","X"]

        # ----------------------------------------------------------------------
        # Time Complexity:
        # - O(m * n): Each cell is visited a constant number of times (DFS might visit
        #             every cell, but only once per capture).
        #
        # Space Complexity:
        # - O(1) if we ignore recursion stack (in-place).
        # - O(m * n) in the worst case for recursion stack in DFS (all 'O's).
