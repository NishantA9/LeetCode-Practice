import heapq
from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:         # Compute squared Euclidean distance and store in minHeap
            dist = (x ** 2) + (y ** 2)  # No need for sqrt since relative distances matter
            minHeap.append([dist, x, y])  # Store (distance, x, y)
        heapq.heapify(minHeap)  # Convert list into a Min-Heap
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)  # Extract the closest point
            res.append([x, y])  # Store only the coordinates
            k -= 1
        return res