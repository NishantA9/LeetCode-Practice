# Definition for a binary tree node. # A TreeNode represents a node in a binary tree with a value, a left child, and a right child.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root): # Helper function to check balance and return height
            if not root: 
                return [True, 0]  # Base case: empty tree is balanced, height = 0
            left, right = dfs(root.left), dfs(root.right) # Recursively check left and right subtrees
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1) # Check if both left and right subtrees are balanced and height difference is <= 1
            return [balanced, 1 + max(left[1], right[1])] # Return [IsBalanced, Height of subtree]
        return dfs(root)[0]  # Extract the boolean result indicating balance