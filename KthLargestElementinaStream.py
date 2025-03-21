import heapq
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k # Initialize a min-heap to store only k largest elements  
        heapq.heapify(self.minHeap)  # Convert list into a heap
        while len(self.minHeap) > k:         # Ensure only k largest elements remain in the heap
            heapq.heappop(self.minHeap)  # Remove smallest elements
        
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)  # Add new value
        if len(self.minHeap) > self.k:  # If heap exceeds k elements
            heapq.heappop(self.minHeap)  # Remove smallest element
        return self.minHeap[0]  # Return the k-th largest element