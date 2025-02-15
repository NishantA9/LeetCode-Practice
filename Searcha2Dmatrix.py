from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0]) # Get the number of rows and columns
        top, bot = 0, ROWS - 1  # Binary search to find the correct row
        while top <= bot:
            row = (top + bot) // 2  # Calculate the middle row
            if target > matrix[row][-1]: # If target is greater than the last element of the row, go down
                top = row + 1
            elif target < matrix[row][0]: # If target is less than the first element of the row, go up
                bot = row - 1
            else: # Target lies within this row
                break
        
        if not (top <= bot):  # If we can't find a valid row
            return False
        
        row = (top + bot) // 2  # Identify the target row
        l, r = 0, COLS - 1 # Binary search within the identified row  # noqa: E741
        while l <= r:
            m = (l + r) // 2  # Calculate the middle column
            if target > matrix[row][m]: # Adjust pointers based on the comparison with the target
                l = m + 1  # noqa: E741
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True  # Target found
        return False  # Target not found