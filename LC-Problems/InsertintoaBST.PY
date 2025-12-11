# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val      # Value of the node
        self.left = left    # Left child node
        self.right = right  # Right child node
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:  # Base case: if tree is empty or reached a leaf
            return TreeNode(val)  # Create new node with the value
        if val > root.val:  # If value is greater than current node
            root.right = self.insertIntoBST(root.right, val)  # Insert in right subtree
        else:  # If value is less than or equal to current node
            root.left = self.insertIntoBST(root.left, val)   # Insert in left subtree
        return root  # Return the root of the modified tree