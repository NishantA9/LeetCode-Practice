from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])  # Get grid dimensions
        visit = set()  # Set to keep track of visited land cells
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        def dfs(r, c): # DFS function to calculate area of an island starting at (r, c)
            if (r < 0 or r == ROWS or # Base case: if out of bounds, water, or already visited → return 0
                c < 0 or c == COLS or
                grid[r][c] == 0 or
                (r, c) in visit):
                return 0
            visit.add((r, c))  # Mark current cell as visited 
            area = 1
            for dr, dc in directions:
                area += dfs(r+dr, c+ dc)
            return area
            # return area
            # return ( 1 + dfs(r + 1, c) +  # down
            #     dfs(r - 1, c) +  # up
            #     dfs(r, c + 1) +  # right
            #     dfs(r, c - 1)    # left
            # ) # Return 1 (current cell) + DFS on all 4 directions
        area = 0  # To track the maximum area found
        for r in range(ROWS):        # Visit every cell in the grid
            for c in range(COLS):
                area = max(area, dfs(r, c))  # If it's land and not visited, explore the island
        return area  # Return the largest island area found

# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         ROWS, COLS = len(grid), len(grid[0])
#         visit = set()  # To track visited cells
#         def dfs(r, c):        # DFS to explore island from (r, c)
#             if (r < 0 or r == ROWS or c < 0 or c == COLS or 
#                 grid[r][c] == 0 or (r, c) in visit):
#                 return 0 # Base case: out of bounds or water or already visited
#             visit.add((r, c))  # Mark cell as visited
#             return (1 +
#                     dfs(r + 1, c) + 
#                     dfs(r - 1, c) + 
#                     dfs(r, c + 1) + 
#                     dfs(r, c - 1))             # Count current cell + 4-directionally connected land
#         area = 0
#         for r in range(ROWS):        # Explore each cell in the grid
#             for c in range(COLS):
#                 area = max(area, dfs(r, c))  # Update max area if needed
#         return area # Return the maximum area found