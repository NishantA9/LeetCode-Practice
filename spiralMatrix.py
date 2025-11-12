from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []         # Initialize result list and boundary pointers
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        while left < right and top < bottom:        # Loop until boundaries cross            
            for i in range(left, right): # Traverse the top row
                res.append(matrix[top][i])
            top += 1  # Move the top boundary down                        
            for i in range(top, bottom): # Traverse the right column
                res.append(matrix[i][right - 1])
            right -= 1  # Move the right boundary left                        
            if not (left < right and top < bottom): # Check if there are remaining rows/columns
                break                        
            for i in range(right - 1, left - 1, -1): # Traverse the bottom row (in reverse)
                res.append(matrix[bottom - 1][i])
            bottom -= 1  # Move the bottom boundary up                        
            for i in range(bottom - 1, top - 1, -1): # Traverse the left column (in reverse)
                res.append(matrix[i][left])
            left += 1  # Move the left boundary right        
        return res # Return the result list in spiral order