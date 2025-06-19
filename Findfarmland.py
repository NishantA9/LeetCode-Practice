class Solution(object):
    def findFarmland(self, land): # TC: O(m * n) & SC: O(m * n)
        rows, cols = len(land), len(land[0])  # Get number of rows and columns
        res = []  # Result list to store top-left and bottom-right corners of each farmland group
        def dfs(r, c): # Depth-First Search to explore the current farmland rectangle
            if r < 0 or r >= rows or c < 0 or c >= cols or land[r][c] != 1:  # Return if out of bounds or not farmland (1)
                return
            land[r][c] = 0  # Mark current cell as visited
            self.bottom = max(self.bottom, r)  # Update the farthest bottom-right cell of this rectangle
            self.right = max(self.right, c)
            # Explore 4 directions (up, down, left, right)
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left
        for r in range(rows): # Iterate over every cell in the land grid
            for c in range(cols):  # If we find unvisited farmland (1), start DFS
                if land[r][c] == 1:
                    self.bottom, self.right = r, c  # Initialize bottom-right corner for this group
                    dfs(r, c)  # Explore the entire rectangle
                    res.append([r, c, self.bottom, self.right])  # Add top-left and bottom-right corners to result
        return res  # Return all farmland group coordinates