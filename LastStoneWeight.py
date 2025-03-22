import heapq
from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones] # Convert stones into a max-heap using negative values
        heapq.heapify(stones)  # Transform the list into a heap
        while len(stones) > 1:  # Continue until one or no stone remains
            first = heapq.heappop(stones)  # Heaviest stone
            second = heapq.heappop(stones)  # Second heaviest stone
            if second > first:  # If they are not equal
                heapq.heappush(stones, first - second)  # Push the remaining weight
        stones.append(0)  # Handle edge case where no stones remain
        return abs(stones[0])  # Return the last remaining stone's weight