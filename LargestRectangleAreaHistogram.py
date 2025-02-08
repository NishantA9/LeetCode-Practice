from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0  # Variable to store the maximum area found
        stack = []  # Monotonic stack to store (index, height) pairs
        for i, h in enumerate(heights):  # Iterate through the heights
            start = i  # Default start index for the current bar
            while stack and stack[-1][1] > h:  # If the current height is less than the top of the stack, calculate the area
                index, height = stack.pop()  # Pop the top bar
                maxArea = max(maxArea, height * (i - index))  # Calculate area
                start = index  # Update start to the index of the popped bar
            stack.append((start, h)) # Append the current bar with its adjusted start index
        for i, h in stack: # Process any remaining bars in the stack
            maxArea = max(maxArea, h * (len(heights) - i))  # Calculate area as if extending to the end
        return maxArea  # Return the maximum area found