class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n  # Last row: only 1 way to go (all right)
        for i in range(m - 1):  # Loop through remaining rows (bottom to top)
            newRow = [1] * n    # Rightmost column always has 1 way (all down)
            for j in range(n - 2, -1, -1):  # Fill row from right to left
                newRow[j] = newRow[j + 1] + row[j]  # Right + Down
            row = newRow  # Move up to the next row
        return row[0]  # Top-left corner contains total unique paths