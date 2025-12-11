class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()        # Columns that are already occupied by queens
        posDiag = set()        # Positive slope diagonals (r + c) occupied
        negDiag = set()         # Negative slope diagonals (r - c) occupied
        res = 0
        def backtrack(r):
            """Place a queen on row r and count all valid completions."""
            nonlocal res
            if r == n:             # If we've placed queens on all rows, we've found a valid solution
                res += 1
                return
            for c in range(n):  # Try placing a queen in each column of the current row
                if c in col or (r + c) in posDiag or (r - c) in negDiag: # If column or either diagonal is occupied, skip this position
                    continue
                col.add(c)                 # Place queen: mark column and diagonals as occupied
                posDiag.add(r + c)
                negDiag.add(r - c)
                backtrack(r + 1)  # Move on to place queen on the next row
                col.remove(c)  # Backtrack: remove the queen and free column/diagonals
                posDiag.remove(r + c)
                negDiag.remove(r - c)
        backtrack(0)         # Start backtracking from row 0
        return res