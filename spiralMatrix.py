from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Initialize result list and boundary pointers
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        # Loop until boundaries cross
        while left < right and top < bottom:
            # Traverse the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1  # Move the top boundary down
            
            # Traverse the right column
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1  # Move the right boundary left
            
            # Check if there are remaining rows/columns
            if not (left < right and top < bottom):
                break
            
            # Traverse the bottom row (in reverse)
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1  # Move the bottom boundary up
            
            # Traverse the left column (in reverse)
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1  # Move the left boundary right

        # Return the result list in spiral order
        return res
