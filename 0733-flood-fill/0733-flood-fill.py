class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        original_colour = image[sr][sc]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        if original_colour == color:
            return image

        def dfs(r, c):
            if(r < 0 or c < 0 or r >= rows or c >= cols or image[r][c] != original_colour):
                return
            image[r][c] = color
            for dr, dc in directions:
                row, col = r+dr, c +dc
                dfs(row, col)
        
        dfs(sr, sc)
        return image

    """
    Clarifying Questions
Is the image always a valid rectangular matrix? (Yes)
Are diagonal pixels considered adjacent? (No, only up/down/left/right)
Can the target color be the same as the starting pixel color? (Yes, if so, image does not change)
Do we need to mutate the original image or return a new one? (Usually mutate in place and return)
What’s the pixel value range? (0 ≤ image[i][j], color < 216)

Approach
If the starting pixel is already the target color, do nothing and return.
Otherwise, use DFS or BFS to visit all connected pixels with the same original color and set them to the new color.
Check boundary conditions to avoid out-of-bounds errors.

Time and Space Complexity
Time: O(m*n) — In the worst case, we might fill every cell in the matrix.
Space: O(m*n) — For the recursion stack in the worst case (or queue if using BFS).

Dry Run (with Example 1)
Input:
image =

[[1,1,1],
 [1,1,0],
 [1,0,1]]
sr = 1, sc = 1, color = 2
Step by Step:
Starting pixel: image[1][1] = 1, orig_color = 1, color = 2
We change (1,1) to 2.
Visit all adjacent pixels with value 1:
(0,1): set to 2, check its neighbors, etc.
(1,0): set to 2
(2,1): value is 0 → skip
(1,2): value is 0 → skip
This continues recursively to all connected '1's.
Final result:
[[2,2,2],
 [2,2,0],
 [2,0,1]]

 #"Perform DFS/BFS from the start pixel, recoloring all connected pixels of the same original color."
    """