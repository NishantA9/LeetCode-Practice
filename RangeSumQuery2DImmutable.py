# brute force -> TLE on LC
class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix  # Store the input matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0  # Initialize result
        for r in range(row1, row2 + 1):  # Loop through rows in the region
            for c in range(col1, col2 + 1):  # Loop through columns in the region
                res += self.matrix[r][c]  # Add up the values in the region
        return res  # Return the sum
    
# another solution -> Acceptable on LC, Optimal O(1) Space

class NumMatrix2:

    def __init__(self, matrix: list[list[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])  # Get number of rows and columns
        self.sumMat = [[0] * (COLS + 1) for r in range(ROWS + 1)]  # Create prefix sum matrix
        for r in range(ROWS):
            prefix = 0  # Initialize prefix sum for each row
            for c in range(COLS):
                prefix += matrix[r][c]  # Add current value to prefix
                above = self.sumMat[r][c+1]  # Get value from above row
                self.sumMat[r+1][c+1] = prefix + above  # Store sum in prefix matrix

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        r1, c1, r2, c2 = r1 + 1, c1 + 1, r2 + 1, c2 + 1  # Shift indices for prefix sum matrix
        bottomRight = self.sumMat[r2][c2]  # Total sum up to bottom right
        above = self.sumMat[r1 - 1][c2]    # Subtract area above
        left = self.sumMat[r2][c1-1]       # Subtract area to the left
        topLeft = self.sumMat[r1 - 1][c1 - 1]  # Add back overlap area
        return bottomRight - above - left + topLeft  # Return the region sum