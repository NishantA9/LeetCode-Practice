import heapq
class MedianFinder:
    def __init__(self):
        self.small = [] # Max heap for the smaller half (use negative values for max behavior)
        self.large = []  # Min heap for the larger half

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)  # Step 1: Add number to max heap (as negative for max behavior)
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:# Step 2: Balance: max of small must be <= min of large
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.small) > len(self.large) + 1:   # Step 3: Balance size so both heaps are nearly equal
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large): # If one heap is bigger, return its top
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2 # If equal size, return average of tops