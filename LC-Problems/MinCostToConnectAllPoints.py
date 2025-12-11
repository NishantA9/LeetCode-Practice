from typing import List
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)  # Step 1: Build the adjacency list # For each point, store its neighbors with cost
        adj = {i: [] for i in range(N)}  # i: list of [cost, node]
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)  # Manhattan distance
                adj[i].append([dist, j])
                adj[j].append([dist, i])
                
        # Step 2: Apply Prim's algorithm
        res = 0  # Result: total cost
        visit = set()  # Track visited nodes
        minH = [[0, 0]]  # Min-heap with [cost, point], start from point 0
        while len(visit) < N:
            cost, i = heapq.heappop(minH)  # Pick the lowest cost edge
            if i in visit:
                continue  # Skip if already visited
            res += cost            # Add the cost to result and mark node as visited
            visit.add(i)
            for neiCost, nei in adj[i]:            # Add all neighbors to the heap
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])
        return res