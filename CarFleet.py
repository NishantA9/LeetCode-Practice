from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []  # Stack to keep track of fleet times
        pair = [[p, s] for p, s in zip(position, speed)] # Pair positions and speeds, then sort by position in descending order #List Comprehension
        for p, s in sorted(pair)[::-1]:  # Reverse sorted order by position
            stack.append((target - p) / s) # Calculate the time for the car to reach the target # decimal division
            if len(stack) >= 2 and stack[-1] <= stack[-2]:# If the current car catches up to the fleet ahead, merge them
                stack.pop()  # Remove the slower fleet's time
        return len(stack) # The size of the stack is the number of fleets