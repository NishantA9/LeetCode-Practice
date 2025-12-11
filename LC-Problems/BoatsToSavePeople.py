from typing import List
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()  # Sort people by weight
        left, right = 0, len(people) - 1  # Two pointers: lightest and heaviest
        res = 0  # Count of boats used
        while left <= right:
            remain = limit - people[right]  # Remaining capacity after heaviest person
            right -= 1  # Put heaviest person on a boat
            res += 1  # Use one boat
            if left <= right and remain >= people[left]:  # If lightest fits with heaviest
                left += 1  # Put lightest person on same boat
        return res  # Return total boats needed