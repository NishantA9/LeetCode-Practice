from typing import List
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val               # Value of the node (True/False)
        self.isLeaf = isLeaf         # Whether this is a leaf node
        self.topLeft = topLeft       # Top-left child node
        self.topRight = topRight     # Top-right child node
        self.bottomLeft = bottomLeft # Bottom-left child node
        self.bottomRight = bottomRight # Bottom-right child node


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n, r, c):  # n: size of current subgrid, r: row, c: column
            if n == 1:  # Base case: single cell
                return Node(grid[r][c] == 1, True)  # Create leaf node with cell value

            mid = n // 2  # Split the grid into 4 quadrants
            topLeft = dfs(mid, r, c)              # Top-left quadrant
            topRight = dfs(mid, r, c + mid)       # Top-right quadrant
            bottomLeft = dfs(mid, r + mid, c)     # Bottom-left quadrant
            bottomRight = dfs(mid, r + mid, c + mid)  # Bottom-right quadrant

            # If all 4 quadrants are leaves with the same value, merge them
            if (topLeft.isLeaf and topRight.isLeaf and
                bottomLeft.isLeaf and bottomRight.isLeaf and
                topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
                return Node(topLeft.val, True)  # Create single leaf node

            # Otherwise, create internal node with 4 children
            return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)

        return dfs(len(grid), 0, 0)  # Start with full grid