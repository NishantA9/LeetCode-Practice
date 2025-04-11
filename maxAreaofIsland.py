from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()  # To track visited cells
        def dfs(r, c):        # DFS to explore island from (r, c)
            if (r < 0 or r == ROWS or c < 0 or c == COLS or 
                grid[r][c] == 0 or (r, c) in visit):
                return 0 # Base case: out of bounds or water or already visited
            visit.add((r, c))  # Mark cell as visited
            return (1 +
                    dfs(r + 1, c) + 
                    dfs(r - 1, c) + 
                    dfs(r, c + 1) + 
                    dfs(r, c - 1))             # Count current cell + 4-directionally connected land
        area = 0
        for r in range(ROWS):        # Explore each cell in the grid
            for c in range(COLS):
                area = max(area, dfs(r, c))  # Update max area if needed
        return area # Return the maximum area found