from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # If the height list is empty, there is no water to trap, so return 0.
        if not height: 
            return 0
        
        # Initialize two pointers: 'l' at the start (left), 'r' at the end (right)
        l, r = 0, len(height) - 1  # noqa: E741
        
        # Initialize variables to store the maximum height seen from the left and right sides.
        leftMax, rightMax = height[l], height[r]
        
        # Initialize the result variable to accumulate the total water trapped.
        res = 0

        # Iterate as long as the left pointer is less than the right pointer.
        while l < r:
            # If the maximum height on the left side is smaller than on the right side,
            # move the left pointer to the right.
            if leftMax < rightMax:
                l += 1  # Move the left pointer rightward  # noqa: E741
                
                # Update the leftMax to the larger of the current leftMax and the new height at 'l'.
                leftMax = max(leftMax, height[l])
                
                # Add the water trapped at the current position (difference between leftMax and current height).
                res += leftMax - height[l]
            else:
                # If the maximum height on the right side is smaller or equal, move the right pointer to the left.
                r -= 1  # Move the right pointer leftward
                
                # Update the rightMax to the larger of the current rightMax and the new height at 'r'.
                rightMax = max(rightMax, height[r])
                
                # Add the water trapped at the current position (difference between rightMax and current height).
                res += rightMax - height[r]
        
        # Return the total amount of water trapped after both pointers meet.
        return res
