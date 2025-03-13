# Definition for a binary tree node.# A TreeNode represents a node in a binary tree with a value, a left child, and a right child.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0  # Variable to store the maximum diameter
        def dfs(curr): # Helper function to compute the height of a node
            if not curr:
                return 0  # If node is None, height is 0
            left = dfs(curr.left) # Recursively calculate the height of left and right subtrees
            right = dfs(curr.right)
            self.res = max(self.res, left + right)  # Update the maximum diameter found so far
            return 1 + max(left, right) # Return height of current node
        dfs(root)  # Start DFS traversal from the root 
        return self.res  # Return the maximum diameter found