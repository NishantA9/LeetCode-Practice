# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True  # Base case: Empty tree is valid
            if not (left < node.val < right): # Check if the current node value violates the BST property
                return False  # Invalid BST
            return (valid(node.left, left, node.val) and valid(node.right, node.val, right)) # Recursively check left and right subtrees
        # Start the recursion with infinite bounds
        return valid(root, float("-inf"), float("inf"))