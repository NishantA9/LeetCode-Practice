from typing import List
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])  # Get dimensions of the matrix
        pac, atl = set(), set()  # To store cells reachable from Pacific and Atlantic oceans
        def dfs(r, c, visit, prevHeight):            # If the cell is out of bounds, already visited, or height is less than previous, return
            if ((r, c) in visit or r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < prevHeight):
                return
            visit.add((r, c))  # Mark the cell as visited
            dfs(r + 1, c, visit, heights[r][c])            # Move in all 4 directions: up, down, left, right
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
        for c in range(COLS):        # Start DFS from all border cells touching the Pacific (top and left edges)
            dfs(0, c, pac, heights[0][c])  # Top row
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])  # Bottom row
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])  # Left column
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])  # Right column
        res = []        
        for r in range(ROWS): # Check all cells: if they can reach both oceans, add to result
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res