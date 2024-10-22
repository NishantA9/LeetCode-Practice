from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize profit to 0
        profit = 0

        # Loop through the price list starting from the second day
        for i in range(1, len(prices)):
            # If today's price is higher than yesterday's, sell today
            if prices[i] > prices[i-1]:
                # Accumulate the profit by adding the difference
                profit += (prices[i] - prices[i-1])
        
        # Return the total accumulated profit
        return profit
