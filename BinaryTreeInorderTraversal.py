# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []  # List to store the inorder traversal result
        def inorder(node):  # Helper function for recursive traversal
            if not node:  # Base case: if node is None
                return
            inorder(node.left)   # Traverse left subtree first
            res.append(node.val) # Visit current node (add to result)
            inorder(node.right)  # Traverse right subtree last
        inorder(root)  # Start traversal from root
        return res     # Return the final result