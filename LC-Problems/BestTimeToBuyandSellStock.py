from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 # Initialize max_profit to store the maximum profit
        min_price = float('inf') # Initialize min_price to store the minimum price encountered so far
        # Traverse each price in the prices list
        for price in prices:
            # If the current price is lower than the minimum price encountered so far
            if price < min_price:
                min_price = price  # Update min_price to the current price
            else:
                potential_profit = price - min_price # Calculate the potential profit if sold at the current price
                max_profit = max(max_profit, potential_profit) # Update max_profit if the potential profit is higher than the current max_profit
        return max_profit  # Return the maximum profit