from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []  # List to store the postorder traversal result
        def postorder(node):  # Helper function for recursive traversal
            if not node:  # Base case: if node is None
                return
            postorder(node.left)   # Traverse left subtree first
            postorder(node.right)  # Traverse right subtree second
            res.append(node.val)   # Visit current node last (add to result)
        postorder(root)  # Start traversal from root
        return res       # Return the final result