from typing import List
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n         # Step 1: Initialize price to all cities as infinity
        prices[src] = 0  # Source has cost 0
        for i in range(k + 1):        # Step 2: Relax all edges up to k + 1 times
            tmpPrices = prices.copy()  # Copy to avoid using updated prices in this round
            for s, d, p in flights:  # s = source, d = destination, p = price
                if prices[s] == float("inf"):
                    continue  # Skip if source is not reachable yet
                if prices[s] + p < tmpPrices[d]:                # Relax the edge
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices  # Update the main price array after each round
        return -1 if prices[dst] == float("inf") else prices[dst] # Step 3: Return the result