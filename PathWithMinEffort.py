from typing import List
import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])  # Grid dimensions
        minHeap = [[0, 0, 0]]  # [effort_so_far, row, col] starting from (0,0)
        visit = set()  # Track visited cells to avoid cycles
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # Right, left, down, up
        while minHeap:  # Dijkstra's algorithm with min heap
            diff, r, c = heapq.heappop(minHeap)  # Get path with minimum effort
            if (r, c) in visit:  # Skip if already visited
                continue
            visit.add((r, c))  # Mark as visited        
            if (r, c) == (ROWS - 1, COLS - 1):  # Reached bottom-right cell
                return diff  # Return minimum effort path found           
            for dr, dc in directions:  # Try all four directions
                newR, newC = r + dr, c + dc  # Calculate next position
                if (
                    newR < 0 or newC < 0 or  # Check boundary conditions
                    newR >= ROWS or newC >= COLS or
                    (newR, newC) in visit  # Skip visited cells
                ):
                    continue
                newDiff = max(diff, abs(heights[r][c] - heights[newR][newC])) # New effort is max of current effort and height difference
                heapq.heappush(minHeap, [newDiff, newR, newC])  # Add to heap
        return 0  # No path found (shouldn't happen per constraints)