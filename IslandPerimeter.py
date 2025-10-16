from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Get grid dimensions
        rows, cols = len(grid), len(grid[0])
        # Keep track of visited cells to avoid counting twice
        visit = set()

        def dfs(i: int, j: int) -> int:
            # When we hit water or boundary, we've found a perimeter edge
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
                return 1
            # If we've visited this cell before, don't count it
            if (i, j) in visit:
                return 0

            # Mark current cell as visited
            visit.add((i, j))
            
            # Explore all 4 directions and sum their perimeter contributions
            # right, down, left, up
            perim = (dfs(i, j + 1) +    # right
                    dfs(i + 1, j) +      # down
                    dfs(i, j - 1) +      # left
                    dfs(i - 1, j))       # up
            return perim

        # Find the first land cell and start DFS from there
        # (Problem guarantees at most one island)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    return dfs(i, j)
        return 0