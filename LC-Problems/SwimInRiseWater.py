from typing import List
import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()  # To keep track of visited cells
        minH = [[grid[0][0], 0, 0]]  # Heap stores [max-elevation-so-far, row, col]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # Right, Left, Down, Up
        visit.add((0, 0))
        while minH:
            t, r, c = heapq.heappop(minH) # Get the cell with minimum "time" (max height so far)
            if r == N - 1 and c == N - 1: # If we reach bottom-right, return the time
                return t
            for dr, dc in directions: # Explore 4 directions
                neiR, neiC = r + dr, c + dc
                if (neiR < 0 or neiC < 0 or neiR == N or neiC == N or (neiR, neiC) in visit): # Boundary check and visited check
                    continue
                visit.add((neiR, neiC))
                heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC]) # Push the neighbor with updated max height/time