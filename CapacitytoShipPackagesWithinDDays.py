from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)  # Min and max possible capacity
        res = right  # Store the minimum found capacity
        def canShip(cap):
            ships, currCap = 1, cap  # Start with 1 ship and full capacity
            for w in weights:
                if currCap - w < 0:  # If current weight doesn't fit
                    ships += 1  # Need a new ship
                    if ships > days:  # Too many ships needed
                        return False
                    currCap = cap  # Reset capacity for new ship
                currCap -= w  # Load weight onto current ship
            return True  # All weights shipped within days
        while left <= right:
            cap = (left + right) // 2  # Try the middle capacity
            if canShip(cap):  # If possible to ship with this capacity
                res = min(res, cap)  # Update result
                right = cap - 1  # Try smaller capacity
            else:
                left = cap + 1  # Try larger capacity

        return res  # Return the minimum capacity found