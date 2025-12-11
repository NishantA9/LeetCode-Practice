import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # Initialize the search space  # noqa: E741
        res = r  # Initialize result to the maximum speed initially
        while l <= r:  # Binary search to find the minimum speed
            k = (l + r) // 2  # Midpoint speed
            hours = 0
            for p in piles: # Calculate hours needed at speed k
                hours += math.ceil(p / k)  # Time to eat each pile
            if hours <= h: # Check if Koko can finish within h hours
                res = min(res, k)  # Update result if current speed is valid
                r = k - 1  # Try to find a slower speed
            else:
                l = k + 1  # Need more speed to finish on time  # noqa: E741
        return res  # Return the minimum valid speed