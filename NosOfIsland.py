from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0], [-1, 0], [0,1], [0,-1]]  # Down, Up, Right, Left
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        def dfs(r, c):        # DFS to sink the island starting from (r, c)
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0":
                return             # Base case: out of bounds or water
            grid[r][c] = "0"  # Mark as visited
            for dr, dc in directions:
                dfs(r + dr, c + dc)  # Explore all 4 directions
        for r in range(ROWS):        # Loop through every cell in the grid
            for c in range(COLS):
                if grid[r][c] == "1":  # Found land
                    dfs(r, c)          # Sink the island
                    islands += 1      # Count it
        return islands