from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0  # rob1 = max amount two houses ago, rob2 = previous house
        for n in nums: # temp is the max if we rob this house or skip it [rob1, rob2, n, n+1, ...]
            temp = max(n + rob1, rob2)
            rob1 = rob2  # Move rob2 back to rob1
            rob2 = temp  # Update rob2 to the best at current house
        return rob2  # rob2 holds the final maximum amount