# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: # Base case: If both trees are empty, they are the same
            return True
        if not p or not q or p.val != q.val: # If one tree is empty and the other is not, or values are different, return False
            return False
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)) # Recursively check if left subtrees and right subtrees are the same