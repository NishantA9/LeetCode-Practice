from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0         # Initialize profit to 0       
        for i in range(1, len(prices)): # Loop through the price list starting from the second day            
            if prices[i] > prices[i-1]: # If today's price is higher than yesterday's, sell today                
                profit += (prices[i] - prices[i-1]) # Accumulate the profit by adding the difference                
        return profit # Return the total accumulated profit