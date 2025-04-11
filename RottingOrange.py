from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()        # Queue to perform BFS on rotten oranges
        time, fresh = 0, 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):        # Step 1: Count fresh oranges and enqueue rotten ones
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        while q and fresh > 0:         # Step 2: BFS to rot adjacent fresh oranges
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] != 1):  # Check bounds and freshness
                        continue
                    grid[row][col] = 2          # Make fresh orange rotten
                    q.append([row, col])        # Add to queue for next minute
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1  # If no fresh oranges left, return time; else, impossible → -1