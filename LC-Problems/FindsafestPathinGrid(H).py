from collections import deque
import heapq
from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        N = len(grid)  # Get the size of the grid (NxN)
        
        # Helper function to check if a cell is within grid bounds
        def in_bounds(r, c):
            return min(r, c) >= 0 and max(r, c) < N

        # Step 1: Precompute the minimum distance from every cell to the nearest dangerous cell
        def preCompute():
            q = deque()  # Queue for BFS
            min_dist = {}  # Dictionary/HashMap to store minimum distances
            
            # Initialize BFS with all dangerous cells (cells with value 1)
            for r in range(N):
                for c in range(N):
                    if grid[r][c]:  # If the cell contains a dangerous value (1)
                        q.append([r, c, 0])  # Add the cell to the queue with distance 0
                        min_dist[(r, c)] = 0  # The minimum distance to a dangerous cell is 0 (itself)
            
            # BFS to calculate minimum distances to nearest dangerous cells
            while q:
                r, c, dist = q.popleft()  # Current cell and distance from the dangerous cell
                # Define neighboring cells (up, down, left, right)
                nei = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
                
                for r2, c2 in nei:  # Loop through the neighbors
                    if in_bounds(r2, c2) and (r2, c2) not in min_dist:
                        # If the neighboring cell is in bounds and hasn't been visited
                        min_dist[(r2, c2)] = dist + 1  # Update the minimum distance
                        q.append([r2, c2, dist + 1])  # Add the neighbor to the queue
            return min_dist  # Return the dictionary containing minimum distances

        # Step 2: Use a max-heap (priority queue) to find the path with maximum safeness
        min_dist = preCompute()  # Get the minimum distance map using the BFS
        maxHeap = [(-min_dist[(0, 0)], 0, 0)]  # Initialize max heap with the top-left corner's distance
        visit = set()  # Set to track visited cells
        visit.add((0, 0))  # Mark the starting cell as visited
        
        # While the heap is not empty, process the current cell
        while maxHeap:
            dist, r, c = heapq.heappop(maxHeap)  # Get the current cell with maximum safeness factor
            dist = -dist  # Negate the distance back to positive (heap stores negatives for max behavior)
            
            # If we reached the bottom-right corner, return the safeness factor
            if (r, c) == (N - 1, N - 1):
                return dist
            
            # Define neighboring cells (up, down, left, right)
            nei = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
            
            for r2, c2 in nei:
                if in_bounds(r2, c2) and (r2, c2) not in visit:
                    # If the neighbor is in bounds and hasn't been visited
                    visit.add((r2, c2))  # Mark the neighbor as visited
                    # Calculate the safeness factor for this neighbor
                    dist2 = min(dist, min_dist[(r2, c2)])  # Take the min of current path and neighbor's safeness
                    # Push the neighbor onto the heap with its safeness factor
                    heapq.heappush(maxHeap, (-dist2, r2, c2))
