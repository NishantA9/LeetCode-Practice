#brute force is not efficient, so we use two pointers to solve this problem which is linear time solution
#Time complexity: O(n)

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize the maximum area to 0
        res = 0
        
        # Initialize two pointers: one at the beginning (left) and one at the end (right) of the list
        l, r = 0, len(height) - 1  # noqa: E741

        # While the two pointers do not cross each other
        while l < r:
            # Calculate the width between the two pointers
            width = r - l
            # Calculate the area formed by the lines at the two pointers
            area = width * min(height[l], height[r])
            # Update the maximum area found so far
            res = max(res, area)

            # Move the pointer pointing to the shorter line inward
            # This is because the area is limited by the shorter line,
            # so moving the longer line won't help increase the area.
            if height[l] < height[r]:
                l += 1  # noqa: E741
            else: #if its greater or if its equal to left pointer
                r -= 1
        
        # Return the maximum area found
        return res
