from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)  # Step after the last stair has 0 cost (destination)
        for i in range(len(cost) - 3, -1, -1):        # Start from the second last real stair and move backwards
            cost[i] += min(cost[i + 1], cost[i + 2])            # Update cost[i] to include the minimum cost of moving forward
        return min(cost[0], cost[1])        # Start from step 0 or step 1, whichever is cheaper