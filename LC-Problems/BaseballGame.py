from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []  # Stack to keep track of scores
        for op in operations:
            if op == "+":  # Add last two scores
                stack.append(stack[-1] + stack[-2])
            elif op == "D":  # Double the last score
                stack.append(2 * stack[-1])
            elif op == "C":  # Invalidate last score
                stack.pop()
            else:
                stack.append(int(op))  # Add new score
        return sum(stack)  # Return total score