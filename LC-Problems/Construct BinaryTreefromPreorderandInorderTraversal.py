# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: # Base Case: If the lists are empty, return None (tree does not exist)
            return None
        root = TreeNode(preorder[0])  # Step 1: First element of preorder is always the root node
        mid = inorder.index(preorder[0])# Step 2: Find the root index in inorder list
        # Step 3: Recursively construct the left subtree Left subtree elements are from start to 'mid' index in inorder  Corresponding preorder elements are from index 1 to mid+1
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        # Step 4: Recursively construct the right subtree Right subtree elements are from mid+1 to end in inorder Corresponding preorder elements are from mid+1 to end
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root         # Return the constructed tree