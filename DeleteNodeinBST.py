# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val      # Value of the node
        self.left = left    # Left child node
        self.right = right  # Right child node
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:  # Base case: node not found
            return root

        if key > root.val:  # Key is in right subtree
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:  # Key is in left subtree
            root.left = self.deleteNode(root.left, key)
        else:  # Found the node to delete
            if not root.left:  # Node has no left child
                return root.right  # Replace with right child
            elif not root.right:  # Node has no right child
                return root.left   # Replace with left child

            # Node has both children: find inorder successor
            cur = root.right  # Start from right subtree
            while cur.left:   # Find leftmost node (smallest in right subtree)
                cur = cur.left
            root.val = cur.val  # Replace current node's value with successor's value
            root.right = self.deleteNode(root.right, root.val)  # Delete the successor
        return root  # Return the root of the modified tree