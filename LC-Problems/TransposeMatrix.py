from typing import List
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(matrix), len(matrix[0])  # original dimensions
        res = [[0] * ROWS for _ in range(COLS)]  # transposed matrix with swapped dims
        for r in range(ROWS):  # iterate rows
            for c in range(COLS):  # iterate cols
                res[c][r] = matrix[r][c]  # place element at flipped position
        return res  # return transposed result