# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not t:  # If the subtree (t) is None, it is always a valid subtree
            return True
        if not s: # If the main tree (s) is None but t is not, t cannot be a subtree
            return False
        if self.sameTree(s, t):  # If the current trees match, return True
            return True
        return (self.isSubtree(s.left, t) or self.isSubtree(s.right, t)) # Recursively check the left and right subtrees of 's'
    
    def sameTree(self, s, t):
        if not s and not t:  # If both trees are empty, they are identical
            return True
        if s and t and s.val == t.val: # If both nodes exist and their values match, recursively check their subtrees
            return (self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right))
        return False  # Otherwise, trees are not identical