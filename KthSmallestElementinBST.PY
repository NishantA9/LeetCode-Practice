# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0  # Counter for visited nodes
        stack = []
        cur = root
        while cur or stack:  # Iterate until all nodes are processed
            while cur:  # Go to the leftmost node
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()  # Process the leftmost node
            n += 1  # Increment count of visited nodes
            if n == k:  # If it's the k-th smallest, return it
                return cur.val
            cur = cur.right # Move to the right subtree