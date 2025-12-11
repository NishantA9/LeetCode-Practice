# Definition for a binary tree node. # A TreeNode represents a node in a binary tree with a value, a left child, and a right child.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:         # Base case: If the tree is empty, return None
            return None
        tmp = root.left         # Swap the left and right child nodes
        root.left = root.right
        root.right = tmp
        self.invertTree(root.left)         # Recursively invert the left subtree
        self.invertTree(root.right)         # Recursively invert the right subtree
        return root         # Return the root node after inversion