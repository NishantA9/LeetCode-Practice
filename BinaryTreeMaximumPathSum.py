# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]  # Global variable to store the maximum path sum
        def dfs(root):         # Helper function for DFS traversal
            if not root:  # Base case: if node is None, return 0
                return 0
            leftMax = dfs(root.left) # Recursive DFS on left and right subtrees
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0) # Ignore negative path sums (choose 0 if negative)
            rightMax = max(rightMax, 0)
            res[0] = max(res[0], root.val + leftMax + rightMax) # Compute max path sum considering the current node as a turning point
            return root.val + max(leftMax, rightMax) # Return the max path sum extending in one direction (left or right)
        dfs(root) # Start DFS traversal
        return res[0] # Return the final maximum path sum