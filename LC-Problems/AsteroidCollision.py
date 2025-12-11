from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []  # Stack to keep track of asteroids
        for a in asteroids:
            # While there is a collision possibility (stack top is right, current is left)
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]  # Calculate the result of collision
                if diff < 0:
                    stack.pop()  # Stack top explodes, check again
                elif diff > 0:
                    a = 0  # Current asteroid explodes
                else:
                    a = 0  # Both explode
                    stack.pop()
            if a:
                stack.append(a)  # Add surviving asteroid to stack
        return stack  # Return the final state