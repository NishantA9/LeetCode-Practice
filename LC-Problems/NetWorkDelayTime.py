from typing import List
import collections
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)        # Step 1: Build the graph as an adjacency list
        for u, v, w in times:        # edges[u] = list of (v, w) where there's an edge u -> v with weight 
            edges[u].append((v, w))
        minHeap = [(0, k)] # Step 2: Use a min-heap to always process the shortest path node first Start from the given node k with time = 0
        visit = set()        # Step 3: Keep track of visited nodes so we don't process them again
        t = 0        # Variable to track the time it takes to reach the farthest node
        while minHeap:        # Step 4: Dijkstra's algorithm loop
            w1, n1 = heapq.heappop(minHeap)            # Get the node with the smallest time so far
            if n1 in visit:            # Skip if this node has already been visited
                continue
            visit.add(n1)            # Mark node as visited
            t = max(t, w1)            # Update the max time seen so far
            for n2, w2 in edges[n1]:            # Go through all neighbors of current node
                if n2 not in visit:                # Only add neighbor if it hasn't been visited yet
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return t if len(visit) == n else -1  # Step 5: If we visited all nodes, return the time it took to reach the farthest, Otherwise, some nodes were unreachable → return -1