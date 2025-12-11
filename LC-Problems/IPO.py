from typing import List
import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfit = []  # Max heap to store profits (using negative values)
        minCapital = [(c, p) for c, p in zip(capital, profits)]         # Min heap to store projects sorted by capital requirement
        heapq.heapify(minCapital)  # Convert to heap structure 
        for _ in range(k):         # Perform at most k projects
            while minCapital and minCapital[0][0] <= w:             # Move all affordable projects to maxProfit heap
                c, p = heapq.heappop(minCapital)  # Get project with lowest capital
                heapq.heappush(maxProfit, -p)    # Add profit to max heap (negative)           
            if not maxProfit:            # If no projects are affordable, break
                break           
            # Choose the most profitable project and update capital
            w += -heapq.heappop(maxProfit)  # Add profit (negate the negative value)      
        return w  # Return final capital