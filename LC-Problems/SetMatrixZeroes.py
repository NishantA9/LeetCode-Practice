from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:      
        ROWS, COLS = len(matrix), len(matrix[0]) # matrix dimensions        
        rows, cols = [False] * ROWS, [False] * COLS # marker arrays: which rows and columns must be zeroed       
        for r in range(ROWS): # First pass: record any row/col that contains a zero
            for c in range(COLS):
                if matrix[r][c] == 0:
                    rows[r] = True  # mark entire row r to be zeroed
                    cols[c] = True  # mark entire column c to be zeroed        
        for r in range(ROWS): # Second pass: set cells to zero if their row or column was marked
            for c in range(COLS):
                if rows[r] or cols[c]:
                    matrix[r][c] = 0  # zero this cell