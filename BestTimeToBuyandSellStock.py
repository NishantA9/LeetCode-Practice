from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize max_profit to store the maximum profit
        max_profit = 0
        # Initialize min_price to store the minimum price encountered so far
        min_price = float('inf')

        # Traverse each price in the prices list
        for price in prices:
            # If the current price is lower than the minimum price encountered so far
            if price < min_price:
                # Update min_price to the current price
                min_price = price
            else:
                # Calculate the potential profit if sold at the current price
                potential_profit = price - min_price
                # Update max_profit if the potential profit is higher than the current max_profit
                max_profit = max(max_profit, potential_profit)

        # Return the maximum profit
        return max_profit
