# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []  # List to store the preorder traversal result
        def preorder(node):  # Helper function for recursive traversal
            if not node:  # Base case: if node is None
                return
            res.append(node.val)  # Visit current node first (add to result)
            preorder(node.left)   # Traverse left subtree
            preorder(node.right)  # Traverse right subtree   
        preorder(root)  # Start traversal from root
        return res      # Return the final result